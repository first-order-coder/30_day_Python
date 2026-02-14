import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return f"{self.question_text} {self.pub_date}" #what is returned here can be seen from Django admin site

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #this creates a relationship each Choice belongs to one Question (one to many relationship: one question --> many choices)
    #-> in the database Django stores this as a column, question_id inside the Choice table
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text

    