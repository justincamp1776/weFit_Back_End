from rest_framework import serializers, status;
from rest_framework.views import APIView;
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Workout
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

    def get_object(self, request, name_id):
        try:
            return Workout.objects.get(name_id=name_id)
        except Workout.DoesNotExist:
            return Http404

    def get(self, request, id):
        workout = Workout.objects.get(name=id)
        serializer = WorkoutSerializer(workout, many=True)
        return serializer.data
    
        
