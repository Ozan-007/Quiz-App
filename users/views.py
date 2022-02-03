from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User

from users.serializers import RegisterSerializer
# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer