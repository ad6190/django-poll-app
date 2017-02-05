import datetime
from django.db import models
from django.utils import timezone
from django.forms import ModelForm

class Question(models.Model):
    question_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
	    now = timezone.now()
	    return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=60)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = '__all__'


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'