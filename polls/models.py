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


class GameInfo(models.Model):
    id = models.AutoField(primary_key=True)
    game_name = models.CharField(max_length=200)
    game_img_url = models.CharField(max_length=200)
    post_num = models.IntegerField(default=0)


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
    create_time = models.DateTimeField(auto_now=True, auto_now_add=True)


class PostList(models.Model):
    id = models.CharField(max_length=255, primary_key=True, default="0")
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    trade_type = models.CharField(max_length=255, default="xxx")
    game_name = models.CharField(max_length=255, default="xxx")
    create_time = models.DateTimeField(auto_now=True, auto_now_add=True)


class PostDetail(models.Model):
    id = models.CharField(max_length=255, primary_key=True, default="0")
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    mate_desc = models.CharField(max_length=255)
    mate_key = models.CharField(max_length=255)
    post_detail = models.TextField(max_length=65530, null=True)
    create_time = models.DateTimeField(auto_now=True, auto_now_add=True)
    trade_type = models.CharField(max_length=255, default="xxx")
    game_name = models.CharField(max_length=255, default="xxx")
    postList = models.OneToOneField(PostList, on_delete=models.CASCADE, default="0")
