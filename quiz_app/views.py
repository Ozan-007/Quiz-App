from rest_framework import generics
from .models import Category, Question, Quiz
from .serializers import CategorySerializer
# Create your views here.

class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        category = self.kwargs['category']
        queryset  = Quiz.objects.filter(category__name = category) # " category__" allows us to reach the parent class attributes.
        return queryset


class QuizDetail(generics.ListAPIView):

    def get_queryset(self):
        title = self.kwargs['title']
        queryset = Question.objects.filter(quiz__title = title)
        return queryset