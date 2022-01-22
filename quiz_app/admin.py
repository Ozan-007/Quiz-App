from django.contrib import admin

from quiz_app.models import Category, Quiz

# Register your models here.
admin.site.register(Category)
admin.site.register(Quiz)