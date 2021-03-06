# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-22 06:57
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True)),
                ('content', models.TextField()),
                ('time', models.DateField()),
                ('likes', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '電影資訊',
                'verbose_name': '電影資訊',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='訂票人')),
                ('phone_number', models.CharField(max_length=11, verbose_name='電話號碼')),
                ('ticket_name', models.CharField(default=' ', max_length=30, verbose_name='電影名稱')),
                ('ticket_time', models.DateTimeField(default=datetime.datetime(2018, 1, 22, 14, 57, 13, 127850), verbose_name='訂票時間')),
            ],
            options={
                'verbose_name_plural': '訂票人信息',
                'verbose_name': '訂票人信息',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='電影名稱')),
                ('num', models.CharField(default='M201', max_length=10, verbose_name='電影編號')),
                ('time', models.DateTimeField(verbose_name='電影開播時間')),
                ('brief', models.TextField(max_length=300, verbose_name='電影票信息')),
                ('seats', models.IntegerField(default=0, verbose_name='剩餘座位')),
            ],
            options={
                'verbose_name_plural': '電影票信息',
                'verbose_name': '電影票信息',
            },
        ),
    ]
