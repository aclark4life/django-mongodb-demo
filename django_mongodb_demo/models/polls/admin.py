from django.contrib import admin  
from .models import Poll, Question, Choice  
  
class ChoiceInline(admin.TabularInline):  
    model = Choice  
    extra = 2  
  
class QuestionInline(admin.TabularInline):  
    model = Question  
    extra = 1  
  
@admin.register(Poll)  
class PollAdmin(admin.ModelAdmin):  
    list_display = ('title', 'pub_date')  
    inlines = [QuestionInline]  
  
@admin.register(Question)  
class QuestionAdmin(admin.ModelAdmin):  
    list_display = ('question_text', 'poll')  
    inlines = [ChoiceInline]  
  
@admin.register(Choice)  
class ChoiceAdmin(admin.ModelAdmin):  
    list_display = ('choice_text', 'question', 'votes')  

