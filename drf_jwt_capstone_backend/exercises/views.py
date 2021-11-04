from rest_framework import serializers, status;
from rest_framework.views import APIView;
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Exercise
from .serializers import ExerciseSerializer
from django.contrib.auth.models import User
from django.http.response import Http404


class ExerciseList(APIView):

    def get(self, request):
        exercises = Exercise.objects.all()
        serializer = ExerciseSerializer(exercises)
        return Response(serializer.data)