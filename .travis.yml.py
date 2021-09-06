language: python
python:
    - 3.9
    - 2.7
install:
    - pip install -r requirements-dev.txt
script:
    -flake8