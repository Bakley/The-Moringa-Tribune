from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_models

import datetime as dt


class tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=60)
    post = tinymce_models.HTMLField()
    editor = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date=today)
        return news

    @classmethod
    def days_news(cls, date):
        news = cls.objects.filter(pub_date__date=date)
        return news


class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
