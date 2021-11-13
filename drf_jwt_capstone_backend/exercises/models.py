from django.db import models


# Create your models here.
class Exercise(models.Model):
    name = models.CharField(max_length=75, blank=True, null=True)
    group = models.CharField(max_length = 75, blank=True, null=True)
    priority = models.CharField(max_length=30, blank=True, null=True)
    plane = models.CharField(max_length=50, blank=True, null=True)
    num_of_limbs = models.CharField(max_length=50, blank=True, null=True)
    push_pull = models.CharField(max_length=50, blank=True, null=True)
    body_part = models.CharField(max_length=50, blank=True, null=True)
    up_low = models.CharField(max_length=50, blank=True, null=True)
    hip_pos = models.CharField(max_length=50, blank=True, null=True)
    agonist = models.CharField(max_length=150, blank=True, null=True)
    collection = models.CharField(max_length=150, blank=True, null=True)
    synergist = models.CharField(max_length=200, blank=True, null=True)
    about = models.CharField(max_length=1000, blank=True, null=True)
    