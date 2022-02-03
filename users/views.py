from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User

from users.serializers import RegisterSerializer
# Create your views here.

class RegisterViews(generics.ListAPIView):
    queryset = User.object.all()
    serializer_class = RegisterSerializer