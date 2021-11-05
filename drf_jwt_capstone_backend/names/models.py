from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.



class Name(models.Model):
    workout_name = models.CharField(max_length=30, blank=True, null=True)