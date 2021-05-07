from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Register, Login

router = DefaultRouter()
router.register(r'users', Login)

urlpatterns = [
    path('register/', Register.as_view()),
    path('', include(router.urls))
]
