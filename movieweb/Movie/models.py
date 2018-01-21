from django.db import models
from datetime import datetime
from django.contrib.auth.models import User



class MovieName(models.Model):
    title = models.CharField(max_length=128, unique=True)
    content = models.TextField()
    time = models.DateField()
    likes = models.ManyToManyField(User)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "電影資訊"
        verbose_name_plural = verbose_name


class Ticket(models.Model):
    name = models.CharField(max_length=30, verbose_name=u"電影名稱")
    num = models.CharField(default='M200', max_length=10, verbose_name=u"電影編號")
    time = models.DateTimeField(verbose_name=u"電影開播時間")
    brief = models.TextField(max_length=300, verbose_name=u"電影票信息")
    seats = models.IntegerField(default=0, verbose_name=u"剩餘座位")
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "電影票信息"
        verbose_name_plural = verbose_name
        

class Person(models.Model):
    name = models.CharField(max_length=10, verbose_name=u"訂票人")
    phone_number = models.CharField(max_length=11, verbose_name=u"電話號碼")
    ticket_name = models.CharField(default=' ', max_length=30, verbose_name=u"電影名稱") # 实际存储为车次，非车票名称
    ticket_time = models.DateTimeField(default=datetime.now(), verbose_name=u"訂票時間")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "訂票人信息"
        verbose_name_plural = verbose_name
    