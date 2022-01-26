from django.urls import path
from quiz_app.serializers import CategoryDetailViewSerializer

from quiz_app.views import CategoryList, CategoryView

urlpatterns = [
    path("category/", CategoryView.as_view(),name="category"),
    path("<category>/", CategoryList.as_view(),name="category"),
]
