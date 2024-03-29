from rest_framework import status;
from rest_framework.views import APIView;
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes

from .models import WorkoutName
from .serializers import WorkoutNameSerializer
from django.contrib.auth.models import User
from django.http.response import Http404



class WorkoutNameList(APIView):

    def get(self, request):
        workout_name = WorkoutName.objects.all()
        serializer = WorkoutNameSerializer(workout_name, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WorkoutNameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    