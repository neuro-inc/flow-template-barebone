import shutil
from pathlib import Path


# >>> Handling project name
PROJECT_NAME = ""
try:
    import asyncio

    import apolo_sdk

    async def get_project_name() -> str:
        async with await apolo_sdk.get() as client:
            return client.config.project_name_or_raise

    PROJECT_NAME = asyncio.run(get_project_name())

except Exception:
    import subprocess

    if shutil.which("apolo"):
        result = subprocess.run(
            ["apolo", "config", "show"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        if result.returncode == 0:
            cli_output = result.stdout.decode().splitlines()
            for line in cli_output:
                if "current project" in line.lower():
                    PROJECT_NAME = line.split()[2]
                    break
if PROJECT_NAME:
    proj_file = Path("./.neuro/project.yml")
    content = proj_file.read_text()
    content = content.replace(
        "# project_name: {project_name}", f"project_name: {PROJECT_NAME}"
    )
    proj_file.write_text("".join(content))
else:
    live_file = Path("./.neuro/live.yml")
    content = live_file.read_text()
    content = content.replace("/$[[ project.project_name ]]/", "")
    live_file.write_text("".join(content))
# <<< Handling project name
