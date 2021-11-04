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
        exercise = Exercise.objects.all()
        serializer = ExerciseSerializer(exercise, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ExerciseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExerciseDetail(APIView):

    def get_object(self, pk):
        try:
            return Exercise.objects.get(pk=pk)
        except Exercise.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        exercise = self.get_object(pk)
        serializer = ExerciseSerializer(exercise)
        return Response(serializer.data)

    def patch(self, request, pk):
        exercise=self.get_object(pk)
        serializer=ExerciseSerializer(exercise, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)