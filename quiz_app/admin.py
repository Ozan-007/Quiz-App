from django.contrib import admin

from quiz_app.models import Answer, Category, Quiz, Question

import nested_admin

# Register your models here.

class AnswerInline(nested_admin.NestedStackedInline):
    model = Answer

class QuestionInline(nested_admin.NestedStackedInline):
    model = Question
    inlines = [AnswerInline]

class QuizAdmin(nested_admin.NestedModelAdmin):
    model = Quiz
    inlines = [QuestionInline]


admin.site.register(Category)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
admin.site.register(Answer)