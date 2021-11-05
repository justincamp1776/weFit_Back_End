from django.db.models.fields.related import ForeignKey
from rest_framework import serializers, status;
from rest_framework.views import APIView;
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Workout
from exercises.models import Exercise
from names.models import Name
from .serializers import WorkoutSerializer
from django.contrib.auth.models import User
from django.http.response import Http404



class WorkoutList(APIView):

    def post(self, request):
        serializer = WorkoutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class WorkoutDetail(APIView):

    def get_object(self, request, pk):
        try:
            return Workout.objects.get(pk=pk)
        except Workout.DoesNotExist:
            return Http404

    def get(self, request, pk):
            workout = Workout.objects.filter(name=pk)
            serializer = WorkoutSerializer(workout, many=True)
            return Response(serializer.data)

    def patch(self, request, pk):
        workout = self.get_object(pk)
        serializer = WorkoutSerializer(workout,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
