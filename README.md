# libpythonpro

Módulo para exemplificar construção de projetos Python no curso PyTools

Nesse curso é ensinado como contribuir com projetos de código aberto.

Suportada a versão Python 3

Link para o curso:
[Python Pro](https://pythonpro.com.br/)

[![Build Status](https://travis-ci.org/geilson25/libpythonpro.svg?branch=master)](https://travis-ci.org/geilson25/libpythonpro)
[![Updates](https://pyup.io/repos/github/geilson25/libpythonpro/shield.svg)](https://pyup.io/repos/github/geilson25/libpythonpro/)
[![Python 3](https://pyup.io/repos/github/pythonprobr/libpythonpro/python-3-shield.svg)](https://pyup.io/repos/github/pythonprobr/libpythonpro/)
[![codecov](https://codecov.io/gh/pythonprobr/libpythonpro/branch/master/graph/badge.svg)](https://codecov.io/gh/pythonprobr/libpythonpro)

Suportada versão 3 de Python

Para instalar no Windows 10:

```console
python3 -m venv .venv
.venv\Scripts\activate
pip install -r requeriments-dev.txt
```

Para atualizar o Pipfile  (com o venv ativo):

```terminal
$ pip install pip-review
$ pip-review --local --interactive
```

Para conferir qualidade de código:

```console
flake8
```

Para atualizar libs:
```terminal
$ pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U
```
Tópicos a serem abordados:
 1. Git
 2. Virtualenv
 3. Pip
 4. Mock
 5. Pipenv
 