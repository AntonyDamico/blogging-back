from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework import generics

from .serializers import RegisterSerializer


class Register(generics.CreateAPIView):
    # Solo usamos el create para registrar usuarios
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
