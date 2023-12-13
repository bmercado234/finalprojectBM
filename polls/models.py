from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin

# Create your models here.

# Question model
class Question(models.Model):
    # Question max length of 200
    question_text = models.CharField(max_length=200)
    # date time field for date question was published
    pub_date = models.DateTimeField("date published")
    # admin interface
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    # check if question was published recently by comparing date with time range
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

# Choice model
class Choice(models.Model):
    # link with question foreign key
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # choice text max length of 200
    choice_text = models.CharField(max_length=200)
    # amount of votes
    votes = models.IntegerField(default=0)