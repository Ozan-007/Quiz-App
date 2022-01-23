from django.contrib import admin

from quiz_app.models import Answer, Category, Quiz, Question

# Register your models here.
admin.site.register(Category)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)