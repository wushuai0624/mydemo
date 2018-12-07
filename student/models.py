from django.db import models

# Create your models here.
class StuInfo(models.Model):
    id = models.IntegerField(default='',primary_key=True)
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    sno = models.CharField(max_length=20)
    score = models.CharField(max_length=20)
class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)