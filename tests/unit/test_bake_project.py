import subprocess
import sys

from cookiecutter.exceptions import FailedHookException
from pytest_cookies.plugin import Cookies  # type: ignore

from tests.utils import inside_dir


def test_project_tree(cookies: Cookies) -> None:
    result = cookies.bake(extra_context={"project_dir": "test-project"})
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "test-project"


def test_run_flake8(cookies: Cookies) -> None:
    result = cookies.bake(extra_context={"project_dir": "flake8-compat"})
    with inside_dir(str(result.project_path)):
        subprocess.check_call(["flake8"])


def test_project_dir_hook(cookies: Cookies) -> None:
    result = cookies.bake(extra_context={"project_dir": "myproject"})
    assert result.exit_code == 0
    result = cookies.bake(extra_context={"project_dir": "my-project"})
    assert result.exit_code == 0
    result = cookies.bake(extra_context={"project_dir": "my?project"})
    assert result.exit_code != 0
    if sys.platform == "win32":
        # Unfortunately, pre_gen hook is called before cookiecutter copies the template
        #  into the TMP dir for rendering.
        # This will not hurt the user,
        #  but the error message will also include a traceback
        assert isinstance(result.exception, OSError)
    else:
        assert isinstance(result.exception, FailedHookException)
    result = cookies.bake(extra_context={"project_dir": "t" * 256})
    assert result.exit_code != 0


def test_project_id_hook(cookies: Cookies) -> None:
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
        result = cookies.bake(extra_context={"project_id": id_})
        assert result.exit_code != 0, id_
        assert isinstance(result.exception, FailedHookException)
    for id_ in correct_ids:
        result = cookies.bake(extra_context={"project_id": id_})
        assert result.exit_code == 0, id_


def test_project_description(cookies: Cookies) -> None:
    descriptions = [
        # " ",
        "Descrition!",
        "123",
        "https://github.com/neuro-inc/cookiecutter-neuro-project/",
    ]
    for descr in descriptions:
        result = cookies.bake(extra_context={"project_description": descr})
        assert result.exit_code == 0, descr
