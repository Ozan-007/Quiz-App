from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterSerializer(UserCreationForm):
    email = serializers.EmailField(required=True,)
    
    class Meta:
        model = User
        fields={"username","email" ,"password", "password2"}
