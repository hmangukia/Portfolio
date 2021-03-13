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
<img src="https://github.com/hmangukia/Portfolio/blob/main/admin_panel_login.png">
  
- Enter the username and password and login where you will see something like this:
<img src="https://github.com/hmangukia/Portfolio/blob/main/admin_panel.png">

- Under Connects, you can add your social media usernames, links(urls) to your profiles, and content(a bit about yourself) you want to show on the connect page
- Under projects, you can add the name(title) of your project, content explaining what your project is all about, and GitHub link to the repo of your project
- Under Posts, you can add blog posts and publish it(or keep it draft)
- Navigate to your site and you will see the projects, blogs and social media profiles added to it
- However, on the left corner of the navbar, it shows “name”. You can change it by going to Portfolio/templates/base.html
- Inside the body and nav tag, find where “Name” is written. Change that to your name and you are good to go!
- For now, the home page is blank. You can add HTML block at Portfolio/templates/index.html