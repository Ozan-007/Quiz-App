from django.urls import path

from quiz_app.views import CategoryView

urlpatterns = [
    path("category/", CategoryView.as_view(),name="category"),
    path("<category>/", CategoryView.as_view(),name="category"),
]
