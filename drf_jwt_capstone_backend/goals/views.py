from rest_framework import status;
from rest_framework.views import APIView;
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Goal
from .serializers import GoalSerializer
from django.contrib.auth.models import User
from django.http.response import Http404

# Create your views here.

class GoalList(APIView):

    def post(self, request):
        serializer = GoalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        song = Goal.objects.all()
        serializer = GoalSerializer(song, many=True)
        return Response(serializer.data)


class GoalCollection(APIView):

     def get(self, request, user_id):
        goals = Goal.objects.filter(user_id=user_id)
        serializer = GoalSerializer(goals, many=True)
        return Response(serializer.data)


class GoalDetail(APIView):

    def get_object(self, pk):
        try:
            return Goal.objects.get(pk=pk)
        except Goal.DoesNotExist:
            return Http404

    def patch(self, request, pk):
        exercise = self.get_object(pk)
        serializer = GoalSerializer(exercise, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, pk):
        goal = self.get_object(pk)
        goal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



