# main/models.py

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

def create_question_and_choices():
    # Create a new question
    q = Question(question_text="What's new?", pub_date=timezone.now())
    q.save()
    
    # Modify and save the question
    q.question_text = "What's up?"
    q.save()
      
    # Cr eate choices for the question
    q.choice_set.create(choice_text='Not much', votes=0)
    q.choice_set.create(choice_text='The sky', votes=0)

#
'''from django.db import models

class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200, verbose_name="Title")  
    tutorial_content = models.TextField(verbose_name="Content") 
    tutorial_published = models.DateTimeField('date published', auto_now_add=True, blank=True)

    def __str__(self):
        return self.tutorial_title
''' ''' '''