import sys

import yaml
from cookiecutter.exceptions import FailedHookException
from pytest_cookies.plugin import Cookies  # type: ignore


def test_flow_tree(cookies: Cookies) -> None:
    result = cookies.bake(extra_context={"flow_dir": "test-flow"})
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "test-flow"


def test_flow_dir_hook(cookies: Cookies) -> None:
    result = cookies.bake(extra_context={"flow_dir": "myflow"})
    assert result.exit_code == 0
    result = cookies.bake(extra_context={"flow_dir": "my-flow"})
    assert result.exit_code == 0
    result = cookies.bake(extra_context={"flow_dir": "my?flow"})
    assert result.exit_code != 0
    if sys.platform == "win32":
        # Unfortunately, pre_gen hook is called before cookiecutter copies the template
        #  into the TMP dir for rendering.
        # This will not hurt the user,
        #  but the error message will also include a traceback
        assert isinstance(result.exception, OSError)
    else:
        assert isinstance(result.exception, FailedHookException)
    result = cookies.bake(extra_context={"flow_dir": "t" * 256})
    assert result.exit_code != 0


def test_flow_id_hook(cookies: Cookies) -> None:
    wrong_ids = [
        "qwe/qwe",
        "qwe?qwe",
        "qwe!qwe",
        "qwe.qwe",
        "qwe%qwe",
        "qwe-qwe",
        "-qwe",
        "qwe-",
        "qwe-qwe",
        "123",
        "1 23",
        "1qwe23",
    ]
    correct_ids = [
        "qwe",
        "q",
        "qwe_qwe",
        "_qwe",
        "qwe_",
        "qwe123",
        "qwe_123",
        "qwe" * 20,
    ]
    for id_ in wrong_ids:
        result = cookies.bake(extra_context={"flow_id": id_})
        assert result.exit_code != 0, id_
        assert isinstance(result.exception, FailedHookException)
    for id_ in correct_ids:
        result = cookies.bake(extra_context={"flow_id": id_})
        assert result.exit_code == 0, id_


def test_flow_description(cookies: Cookies) -> None:
    descriptions = [
        # " ",
        "Descrition!",
        "123",
        "https://github.com/neuro-inc/flow-template/",
    ]
    for descr in descriptions:
        result = cookies.bake(extra_context={"flow_description": descr})
        assert result.exit_code == 0, descr


def test_flow_name(cookies: Cookies) -> None:
    result = cookies.bake()

    assert result.exit_code == 0
    project_yml = result.project_path / ".neuro" / "project.yml"
    project_yml_content = yaml.safe_load(project_yml.read_text())

    assert "project_name" in project_yml_content
