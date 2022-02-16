from django.db import models
from django.contrib import admin
from django.urls import reverse
# Create your models here.
class Users(models.Model):
    title=models.CharField(max_length=32,default='无标题')
    content=models.CharField(max_length=1000,default='')

    def __str__(self):
        return self.title