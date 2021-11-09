from rest_framework import serializers
from .models import Goal


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ['id', 'selected_goal', 'custom_goal', 'user']