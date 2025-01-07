Apolo Platform Flow Template v25.01.07 (2025-01-07)
===================================================


Features
--------


- This version includes changes to add schema references for YAML language server in the configuration files. These changes aim to improve the development experience by providing schema validation and autocompletion for the YAML files.

  Improvements to YAML files:

  - {{cookiecutter.flow_dir}}/.apolo/live.yml: Added schema reference for the YAML language server to enable schema validation and autocompletion.
  - {{cookiecutter.flow_dir}}/.apolo/project.yml: Added schema reference for the YAML language server to enable schema validation and autocompletion. ([#279](https://github.com/neuro-inc/flow-template-barebone/issues/279))

- This version includes changes to Dockerfile to the new runtime image

  Changes:

  {{cookiecutter.flow_dir}}/Dockerfile: Upgraded image to v24.12.0 ([#280](https://github.com/neuro-inc/flow-template-barebone/issues/280))


Misc
----

- Use ".apolo" directory instead of ".neuro" and apolo* files istead of neuro* to configure apolo-flow. ([#288](https://github.com/neuro-inc/flow-template-barebone/issues/288))


Apolo Platform Flow Template v24.11.11 (2024-11-11)
===================================================


No significant changes.


Neuro Platform Project Template v23.07.10 (2023-07-10)
======================================================


No significant changes.


Neuro Platform Project Template v22.05.10 (2022-05-10)
======================================================


Features
--------


- Use full storage and volume URIs in the template ([#21](https://github.com/neuro-inc/cookiecutter-neuro-project-barebone/issues/21))

- Added project owner and role generation in post-generate hooks. ([#30](https://github.com/neuro-inc/cookiecutter-neuro-project-barebone/issues/30))


Neuro Platform Project Template v22.03.21 (2022-03-21)
======================================================


Features
--------


- Make default job runnable by providing sample bash script. ([#8](https://github.com/neuro-inc/cookiecutter-neuro-project-barebone/issues/8))


Neuro Platform Project Template v22.03.10 (2022-03-10)
======================================================


Features
--------


- Created a barebone Neu.ro project template based on the [`neuro-inc/cookiecutter-neuro-project`](https://github.com/neuro-inc/cookiecutter-neuro-project) ([#4](https://github.com/neuro-inc/cookiecutter-neuro-project-barebone/issues/4))
