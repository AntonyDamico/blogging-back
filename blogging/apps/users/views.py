from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import RegisterSerializer, LoginSerializer


class Register(generics.CreateAPIView):
    # Solo usamos el create para registrar usuarios
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)


class Login(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


