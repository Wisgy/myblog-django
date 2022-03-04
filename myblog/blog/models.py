from django.db import models
from django.contrib import admin
from django.urls import reverse
# Create your models here.
class articles(models.Model):
    title=models.CharField(max_length=32,default='无标题')
    content=models.CharField(max_length=255,default='')

    def __str__(self):
        return self.title

    def contentstr(self):
        return self.content[:5]+"......"

    class Meta:
        db_table="blog_users"
        verbose_name='浏览文章信息'
        verbose_name_plural='文章管理'

class comments(models.Model):
    author=models.CharField(max_length=10,default="匿名")
    content=models.CharField(max_length=255,default='')
    artid=models.IntegerField(default=0)

    def __str__(self):
        return self.content[0:5]+"....."

    class Meta:
        db_table="blog_comments"
        verbose_name='浏览评论信息'
        verbose_name_plural='评论管理'