
# Create your models here.
from django.db import models


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)    # Poll question
    pub_date = models.DateTimeField('date published')    # when it was created

    def __str__(self):
        return self.question_text   # display the question nicely in admin


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # link to a question
    choice_text = models.CharField(max_length=200)      # the text of choice
    votes = models.IntegerField(default=0)    # Number votes this choice has received

    def __str__(self):
        return self.choice_text