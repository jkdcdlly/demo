from django.db import models
from django.utils import timezone
import datetime


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Trade(models.Model):
    id = models.CharField(max_length=255, default="0", primary_key=True)
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    threads = models.IntegerField(default=0)
    posts = models.IntegerField(default=0)


class WonList(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    id = models.CharField(max_length=255, primary_key=True, default="0")
    trade = models.ForeignKey(Trade, on_delete=models.CASCADE)


class PostHome(models.Model):
    id = models.CharField(max_length=255, primary_key=True, default="0")
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    create_time = models.DateTimeField()


class PostList(models.Model):
    id = models.CharField(max_length=255, primary_key=True, default="0")
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    trade_type = models.CharField(max_length=255)
    game_name = models.CharField(max_length=255)
    create_time = models.DateTimeField()


class PostDetail(models.Model):
    id = models.CharField(max_length=255, primary_key=True, default="0")
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    mate_desc = models.CharField(max_length=255)
    mate_key = models.CharField(max_length=255)
    create_time = models.DateTimeField()
    trade_type = models.CharField(max_length=255)
    game_name = models.CharField(max_length=255)
    postList = models.OneToOneField(PostList, on_delete=models.CASCADE, default="0")
