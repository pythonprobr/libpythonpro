language: python
python:
    - 3.9
install:
    - pip install -r requirements-dev.txt
script:
    -flake8