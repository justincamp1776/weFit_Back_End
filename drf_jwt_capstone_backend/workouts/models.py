from django.db import models
from django.db.models.fields.related import ForeignKey
from exercises.models import Exercise
from names.models import Name

# Create your models here.



class Workout(models.Model):
    name = models.ForeignKey(Name, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)