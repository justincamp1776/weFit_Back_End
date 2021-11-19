from django.contrib.auth import get_user_model
from .serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework.views import APIView;
from rest_framework import generics
from django.http.response import Http404
from .models import User
from rest_framework.permissions import AllowAny
User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

class UserDetail(APIView):
    
    # permission_classes = (AllowAny)

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = RegistrationSerializer(user)
        return Response(serializer.data)