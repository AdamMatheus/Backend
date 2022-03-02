from rest_framework.generics import CreateAPIView

from .serializers import RegisterSerializer
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User


class RegisterAPI(CreateAPIView):
    queryset= User.objects.all()
    serializer_class=RegisterSerializer
