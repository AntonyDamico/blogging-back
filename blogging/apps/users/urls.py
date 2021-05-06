from django.urls import path, include
from .views import Register


urlpatterns = [
    path('users/register', Register.as_view())
]
