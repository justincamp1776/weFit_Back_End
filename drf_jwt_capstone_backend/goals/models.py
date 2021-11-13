from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

User = get_user_model()

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    selected_goal = models.CharField(max_length = 100, default="Burn Fat and Lose Weight")
    custom_goal = models.CharField(max_length=250, default="I want to follow this program every week for 1 month.")
    complete = models.BooleanField(default=False)
    
  

