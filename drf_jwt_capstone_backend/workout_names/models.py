from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields.related import ForeignKey


# Create your models here.

User = get_user_model()

class WorkoutName(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True, null=True)