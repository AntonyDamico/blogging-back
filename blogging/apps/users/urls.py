from django.urls import path, include
from .views import UserViewSet


urlpatterns = [
    path('users/login', UserViewSet.as_view())
]
