# LAB - Class 28


## Project:

Django CRUD

___

## Author:

Eden Brekke
___


### Links and Resources

Most of what I've done here was from the Demo JB provided during lecture.
___


## Setup

```python
py -m venv .venv
.\.venv\Scripts\activate
pip install django
django-admin startproject snacks_project .
python manage.py migrate
python manage.py runserver
python manage.py startapp snacks
# TUV 
# T - templates
# U - URLs
# V - Views 
# Add app to settings then make migrations
python manage.py makemigrations app_name
python manage.py migrate
# make a super user for the site (admin)
python manage.py createsuperuser
# Username: admin
# password: admin
# test everything is working by 
python manage.py runserver
# going to local host server and adding /admin to the end of the path
```
___


## Tests

How do you run tests?

```python
from django.test import TestCase
#create a class that extends the TestCase class and then run command:
python manage.py test
```

Any tests of note?

* All of them are neat! I like that you can test that content is rendering correctly on your page! 

Describe any tests that you did not complete, skipped, etc

* all tests pass!

___