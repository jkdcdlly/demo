from django.db import models


# Create your models here.

class GameInfo(models.Model):
    id = models.AutoField(primary_key=True)
    game_name = models.CharField(max_length=200)
    game_img_url = models.CharField(max_length=200)
    post_num = models.IntegerField(default=0)


class PostHome(models.Model):
    id = models.CharField(max_length=255, primary_key=True, default="0")
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)


class PostList(models.Model):
    id = models.CharField(max_length=255, primary_key=True, default="0")
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    trade_type = models.CharField(max_length=255, default="xxx")
    game_name = models.CharField(max_length=255, default="xxx")
    create_time = models.DateTimeField(auto_now_add=True)


class PostDetail(models.Model):
    id = models.CharField(max_length=255, primary_key=True, default="0")
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    mate_desc = models.CharField(max_length=255)
    mate_key = models.CharField(max_length=255)
    post_detail = models.TextField(max_length=65530, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    trade_type = models.CharField(max_length=255, default="xxx")
    game_name = models.CharField(max_length=255, default="xxx")
    postList = models.OneToOneField(PostList, on_delete=models.CASCADE, default="0")
