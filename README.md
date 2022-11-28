# python github aciions tutorial


[python github actions w/ tox and pre-commit $anthonywritescode @2020](https://www.youtube.com/watch?v=KKJL8bM4cis)


## Dev Setup

> creating virtual environment and installing dependencies

```powershell
$ mkdir .venv
$ pipenv install --dev
```

> activating virtual environment

```powershell
$ pipenv shell
```

> running the application

```powershell
$ python main.py
```

> running pytest tests

```powershell
$ pytest
```

> running tox 

- for testing app on different python environment

```powershell
$ tox
```

- for testing app on the python interpretter installed in the system

```powershell
$ tox -e py
```

## Setup

make sure python is installed, and pipenv is installed in the system.

> installing pipenv

```powershell
$ pip install pipenv
```

> setup virtual environment, installing dependencies

```powershell
$ mkdir .venv
$ pipenv install
```

> running the application

```powershell
$ pipenv run python main.py
```

(or)

```powershell
$ pipenv shell
$ python main.py
```