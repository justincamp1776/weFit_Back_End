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


class GoalDetail(APIView):

    def get(self, request, user_id):
        goal = Goal.objects.get(user_id=user_id)
        serializer = GoalSerializer(goal)
        return Response(serializer.data)

