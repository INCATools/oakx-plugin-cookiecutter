# oakx-plugin-cookiecutter
A [Cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) template for [OAK](https://incatools.github.io/ontology-access-kit/) plugin modules.

See:

- [how to write a plugin](https://incatools.github.io/ontology-access-kit/howtos/write-a-plugin.html)

## Getting started

First, install the [cruft](https://github.com/cruft/cruft) package. Cruft enables keeping projects up-to-date with future updates made to this original template.

```
pip install cruft
```

Next, create a project using the `oakx-plugin-cookiecutter` template.

```
cruft create https://github.com/incatools/oakx-plugin-cookiecutter
```

This kickstarts an interactive session where you declare the following:
 - `project_name`: Name of the project. [defaults to: Project_X]
 - `project_description`: Description of the project. [defaults to: This is the project description.].
 - `file_name`: The name of the main python file. [defaults to: `main` for `main.py`]
 - `greeting_recipient`: Just a string that will be displayed when the boilerplate code is invoked. [defaults to: `World` as in `Hello, World!`]
 - `author`: The author of the project. [defaults to: Harshad Hegde <hhegde@lbl.gov>]
 - `github_token_for_doc_deployment`: The github token name for document deployment using `Sphinx`. [defaults to: `GH_TOKEN`]
 - `github_token_for_pypi_deployment`: The github token name which aligns with your autogenerated PyPI token for making releases. [defaults to: `PYPI_TOKEN`]

This will generate the project folder abiding by the template configuration specified by `oakx-plugin-cookiecutter` in the [`cookiecutter.json`](https://github.com/INCATools/oakx-plugin-cookiecutter/blob/main/cookiecutter.json) file. 

# What does this do?

The following files and directories are autogenerated in the project:

 - Github wokflows:
   - For code quality checks (`qc.yml`)
   - Documentation deployment (`deploy-docs.yml`)
   - PyPI deployment (`pypi-publish.yml`)
 - `docs` directory with `Sphinx` configuration files and an `index.rst`file.
 - `src` directory structure with the `project_name` directory within it.
   - Within the `project_name` directory, there are 2 python files:
     - `main_file.py`
     - `cli.py` for [`click`](https://click.palletsprojects.com) commands.
 - `tests` directory with a very basic test.
 - `poetry` compatible `pyproject.toml` file containing minimal package requirements.
 - `tox.ini` file containing configuration for:
   -  `coverage-clean`
   -  `lint`
   -  `flake8`
   -  `mypy`
   -  `docstr-coverage`
   -  `pytest`
- `README.md` file containing `project_description` value entered during setup.


# Further setup

## Install `poetry`
Install `poetry` if you haven't already. Also `poetry-dynamic-versioning` for obvious reasons.
```
pip install poetry poetry-dynamic-versioning
```
## Install dependencies
```
poetry install
```

## Run `tox` to see if the setup works
```
poetry run tox
```

This should run all the bullets mentioned above under the `tox` configuration and ideally you should see the following at the end of the run:
```
  coverage-clean: commands succeeded
  lint: commands succeeded
  flake8: commands succeeded
  mypy: commands succeeded
  docstr-coverage: commands succeeded
  py: commands succeeded
  congratulations :)
```

And as the last line says: `congratulations :)`!! Your project is ready to evolve!

# Final test to see everything is wired properly

On the command line, type the `project_name`. In this example, `ABCD`:
```
ABCD run
```
Should return `Hello, **greeting_recipient value chosen during setup**`

# Future updates to the project's boilerplate code

In order to be up-to-date with the template, first check if there is a mismatch between the project's boilerplate code and the template by running:
```
cruft check
```

This indicates if there is a difference between the current project's boilerplate code and the latest version of the project template. If the project is up-to-date with the template:
```
SUCCESS: Good work! Project's cruft is up to date and as clean as possible :).
```

Otherwise, it will indicate that the project's boilerplate code is not up-to-date by the following:
```
FAILURE: Project's cruft is out of date! Run `cruft update` to clean this mess up.
```

For viewing the difference, run `cruft diff`. This shows the difference between the project's boilerplate code and the template's latest version.

After running `cruft update`, the project's boilerplate code will be updated to the latest version of the template.

