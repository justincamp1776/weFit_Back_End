from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

User = get_user_model()

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=100, default="increase strength")
  

