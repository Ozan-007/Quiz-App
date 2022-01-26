from rest_framework import serializers

from quiz_app.models import Category, Quiz


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ( "id" , "name", "question_count")



class CategoryDetailView(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ("title", "question_count")