from rest_framework import serializers
from .models import WorkoutName


class WorkoutNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkoutName
        fields = ['id', 'name', 'user_id']