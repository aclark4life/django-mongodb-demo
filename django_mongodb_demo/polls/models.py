from django.db import models  
from django_mongodb_backend.models import EmbeddedModel
from django_mongodb_backend.fields import EmbeddedModelArrayField

  
class Poll(models.Model):  
    title = models.CharField(max_length=200)  
    description = models.TextField(blank=True)  
    pub_date = models.DateTimeField('date published')  
  
    def __str__(self):  
        return self.title  
  
  
class Question(models.Model):  
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='questions')  
    question_text = models.CharField(max_length=200)  
  
    def __str__(self):  
        return self.question_text  
  
  
class Choice(models.Model):  
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')  
    choice_text = models.CharField(max_length=200)  
    votes = models.IntegerField(default=0)  
  
    def __str__(self):  
        return self.choice_text  



class EmbeddedChoice(EmbeddedModel):
    choice_text = models.CharField(max_length=200)  
    votes = models.IntegerField(default=0)  
  
    def __str__(self):  
        return self.choice_text  


class EmbeddedQuestion(EmbeddedModel):  
    question_text = models.CharField(max_length=200)  
    choices = EmbeddedModelArrayField(EmbeddedChoice, blank=True, null=True)
  
    def __str__(self):  
        return self.question_text  


class EmbeddedPoll(models.Model):
    title = models.CharField(max_length=200)  
    description = models.TextField(blank=True)  
    pub_date = models.DateTimeField('date published')  
    questions = EmbeddedModelArrayField(EmbeddedQuestion)
  
    def __str__(self):  
        return self.title  
