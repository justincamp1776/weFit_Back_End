from rest_framework import status;
from rest_framework.views import APIView;
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Name
from .serializers import NameSerializer
from django.contrib.auth.models import User
from django.http.response import Http404



class NameList(APIView):

    def get(self, request):
        workout_name = Name.objects.all()
        serializer = NameSerializer(workout_name, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NameDetail(APIView):

    def get_object(self, pk):
        try:
            return Name.objects.get(pk=pk)
        except Name.DoesNotExist:
            return Http404

    def delete(self, request, pk):
        name = self.get_object(pk)
        name.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)