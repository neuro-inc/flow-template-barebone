Release instructions
====================

Apolo Flow [uses `master` branch](https://github.com/neuro-inc/neuro-flow/blob/ac659ff0f1f17c6d820cd2126e3769973dfde86b/neuro_flow/cli/project_template.py#L10) to scaffold projects, so to do a release we need to update `master` branch.


Instructions:
------------

1. Merge all necessary PRs and ensure that `master` is green, update your local master branch:
    ```
    $ git checkout master
    $ git pull origin
    ```
2. Test `master` manually:
    ```
    $ cookiecutter gh:neuro-inc/flow-template-barebone -c master
    flow_name [My Flow]:
    flow_dir [my flow]:
    flow_id [my_flow]:
    $ cd my flow
    $ ls
    Dockerfile  apt.txt  requirements.txt  results
    $ apolo-flow build train
    $ apolo-flow run train
    ...
    ```
3. Generate changelog:
    - `make changelog-draft` - verify changelog looks valid
    - `make changelog` - delete changelog items from `CHANGELOG.d` and really modify [CHANGELOG.md](./CHANGELOG.md)
    - `git add CHANGELOG* version.txt`
    - `git commit -m "Update version and changelog for $(cat version.txt) release"` - commit changelog changes in **local** repository
    - `git tag $(cat version.txt)` - mark latest changes as a release tag
    - `git push && git push --tags` - push the updated changelog and assigned tag to the remote repository
    - Note, this `master` branch update will trigger CI

Notes:
------

- When CI is triggered:
    - Each open PR (even draft PR) agains `master`.
