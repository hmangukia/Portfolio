# Portfolio

[![made with &hearts in Django](https://img.shields.io/badge/made%20with%20%E2%9D%A4%20in-Django-red.svg)](http://shields.io/#your-badge)

## Installation

- Fork the repository and clone it into your PC
- Open CMD and navigate into the cloned project folder
- Create a virtual environment by `python3 -m venv <name_of_virtualenv>`
- Activate the created virtual environment by `<name_of_virtualenv>\Scripts\activate`
- We need to install Django and Django-environ in order to run our project successfully. For that, run `pip install django` and `pip install django-environ`
- In the same directory as settings.py, create a file called ‘.env’. Generate a Django secret key from https://djecrety.ir/, copy that and add it to your .env file as SECRET_KEY=<the secret key you copied>. Make sure you don’t use quotations around strings.
- Before running the project, we need to run `python manage.py makemigrations` and `python manage.py migrate` to make and apply migrations
- Now, run the project by `python manage.py runserver`
- You will see something like this on the CMD, this means you have successfully installed the Portfolio project:
```
March 12, 2021 - 14:59:22
Django version 3.0.3, using settings 'Portfolio.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
- Now press ctrl+c to stop the server
- Wonderful thing about Django is it provides admin panel, for that we need to create the superuser by running `python manage.py createsuperuser`
- Enter the username, email and password(you wont be able to see the typed password on the screen)
- Now again run the server by `python manage.py runserver`
- Navigate to 127.0.0.1:8000/admin
- You will see something like this:
<img width="400" src="https://github.com/hmangukia/Profile/blob/main/admin_panel.png">