from rest_framework import serializers
from .models import Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'priority', 'plane', 'num_of_limbs', 'push_pull', 'body_part', 
        'up_low', 'hip_pos', 'agonist', 'antagonist', 'synergist', 'about']
