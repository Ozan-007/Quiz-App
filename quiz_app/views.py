from django.shortcuts import render
from rest_framework import generics
from .models import Category, Quiz
from .serializers import CategorySerializer
# Create your views here.

class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        category = self.kwargs['category']
        queryset  = Quiz.objects.filter(category__name = category)
        return queryset