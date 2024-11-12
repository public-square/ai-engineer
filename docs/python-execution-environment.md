# Python Execution Environment
The application requires python 3.12 with pip and poetry. A local virtual
execution environment is utilized to avoid version conflicts with other python
on the system.

Note that most examples below must be executed in the root directory of the
project. Installation of version 3.12 on the system can run from anywhere, but
commands that modify the virtual execution environment assume the user is in
the root directory of the application.

## Ubuntu System Execution Environment
### System Python 3.12
```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt install python3.12 python3.12-venv
```

### System Poetry
Poetry is used to manage the virtual execution environment for the application.
This must be installed for python 3.12 at the system level and configured to
create the virtual execution environment for the application.
```bash
python3.12 -m pip install poetry
python3.12 -m poetry config virtualenvs.in-project true
python3.12 -m poetry config virtualenvs.create true
```

## Local Virtual Execution Environment
From the application root, launch a poetry shell to instantiate the virtual
execution environment. Install poetry locally for the application, and use the
local instance of poetry to install application dependencies.

This avoids conflicts with other python projects on the same system.

```bash
echo exit | python3.12 -m poetry shell
.venv/bin/python -m pip install poetry
.venv/bin/python -m poetry install
```

### Manual Dependency Addition
If you extend this software and new requirements are needed, use poetry in the
virtual execution environment to make them available at run time.
```bash
.venv/bin/python -m poetry add ${dependency}
```

If you have a requirements.txt file, this will add them to poetry:
```bash
cat requirements.txt | xargs -I % sh -c '.venv/bin/python -m poetry add "%"'
```

### Local Execution Environment Rebuild
If the local instance of python or dependencies becomes corrupted, or to
validate that poetry provides a complete execution environment, simply delete
the virtual environment and recreate it.

Be sure that `poetry.lock` and `pyproject.toml` are up to date and complete
before taking these steps. Any local modules that have not been installed with
poetry may be lost.

```bash
rm -rf .venv
python3.12 -m poetry config virtualenvs.in-project true
python3.12 -m poetry config virtualenvs.create true
echo exit | python3.12 -m poetry shell
.venv/bin/python -m pip install poetry
.venv/bin/python -m poetry install
```

## Common Failures
If pip becomes corrupted, install latest version manually. The local instance
should be used to manage dependencies and the system instance associated with
the correct version of python is used for initial setup.

### Local Pip
```bash
curl -sS https://bootstrap.pypa.io/get-pip.py | .venv/bin/python
```

### System Pip
```bash
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.12
```

