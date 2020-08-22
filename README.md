# decisionmaker

## Setup

### Installation

**Requirements**

- Python 3.8.*
- Pip
- Django 3.0.*
- All the required libraries installed (Installation described below)

### Environment setup

Setting up the environment with requirements.txt:

- Run `pip install -r requirements.txt` or `pip install --user --requirement requirements.txt`
- If you want to update requirements file, add necessary packages and run `pip freeze > requirements.txt`

Run usual django commands (manage.py file is in the main **decisionmaker** directory):

- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py migrate --run-syncdb`
- `python manage.py runserver`

### About the website

Includes one django app: questions

This app allows a user to enter a question and add all possible options and get a random option chosen to help make a decision.
It's kind of a coin flip, but with a possibility to randomly choose from a wide range of options.

Design/files:
- static directory includes bootstrap css, js, and custom js necessary for templates and favicon (static/images)
- templates extend base template (scripts, main design)

Technical details:
- This is a model-free app, all data is stored in sessions and model tests are not needed
- There are only two views: main (homepage) and result
- There are two forms specified in forms.py: question and answers
- .gitattributes file is there to make sure github marks this repo as python