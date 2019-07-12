# libpythonpro

Módulo para exemplificar construção de projetos Python no curso PyTools

Nesse curso é ensinado como contribuir com projetos de código aberto

Link para o curso [Python Pro](https://www.python.pro.br/)

[![Build Status](https://travis-ci.org/pythonprobr/libpythonpro.svg?branch=master)](https://travis-ci.org/pythonprobr/libpythonpro)
[![Updates](https://pyup.io/repos/github/pythonprobr/libpythonpro/shield.svg)](https://pyup.io/repos/github/pythonprobr/libpythonpro/)
[![Python 3](https://pyup.io/repos/github/pythonprobr/libpythonpro/python-3-shield.svg)](https://pyup.io/repos/github/pythonprobr/libpythonpro/)
[![codecov](https://codecov.io/gh/pythonprobr/libpythonpro/branch/master/graph/badge.svg)](https://codecov.io/gh/pythonprobr/libpythonpro)

Suportada versão 3 de Python

Para instalar:

```console
pip install pipenv
pipenv install --dev
```

Para conferir qualidade de código:

```console
pipenv run flake8
```

Tópicos a serem abordados:
 1. Git
 2. Virtualenv
 3. Pip
 4. Mock
 5. Pipenv
 
Resumo do fluxo feature and branch para contribuir em projetos open source:
1) Faça um fork do repositório para sua conta.
2) Clone o projeto na sua máquina local;
3) Adicione o repositório a referencia para o repositório remoto original;
    *  git remote add \<apelido para repositório remoto\> \<url\>
4) Faça fetch do repositório remoto do qual o fork foi feito que podemos chamar de upstream;
    * git fetch \<nome do repositório remoto (upstream)\>
5) Faça checkout para branch local master gerado a partir do remoto upstream e merge do remoto (ou simplesmente pull);
    * git checkout master
6) Criar branch local a partir do master e codificar o que for necessário neste branch;
7) Comitar e dar push com esse branch remoto;
8) Faça um pull request;
9) Se não for aceito e precisar de modificação, modifique localmente e repita a partir do passo 4;  
10) Sendo aceito, Faça fetch no repositório remoto;
11) Sendo aceito faça push para o remoto origin do fork minha conta remota.
        * git push 
