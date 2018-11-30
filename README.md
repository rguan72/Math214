# Getting started

1. Install git: http://git-scm.com/download/mac
2. Run
`$ python --version` to make sure you have python 3 installed.
If not, install python 3.
3. Install pipenv:
`$ pip install --user pipenv`
4. Get in the pipenv shell:
`$ pipenv shell`
5. If you get a "TypeError: 'module' object is not callable" error, run:
`$ pipenv run pip install pip==18.0`
`$ pipenv install`
`$ pipenv shell`
6. Make kaggle account.
7. Download kaggle.json from My Account -> Create API token and place in your ~/.kaggle folder.
