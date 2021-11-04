from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import DateField

# Create your models here.

# To add new columns to the authentication_user table include the properties
# in the model below
# In order for the new columns to appear in the database run:
# 1. python manage.py makemigrations
# 2. python manage.py migrate


class User(AbstractUser):
    middle_name = models.CharField(max_length=20)
    birth_date = models.DateField(null=True, blank=True)
    weight = models.CharField(max_length=50,null = True, blank = True)
    height = models.IntegerField(null = True, blank = True)
