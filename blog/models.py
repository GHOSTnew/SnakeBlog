from django.db import models
from django.contrib.auth.models import User
from SnakeBlog.utils import bbcode


class Article(models.Model):
    title = models.CharField(max_length=120, primary_key=True)
    content = models.TextField()
    content_html = models.TextField(editable=False, blank=True, null=True)
    author = models.ForeignKey(User, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=True, verbose_name="Date de parution")

    def __str__(self):
        return self.title

    def save(self):
        self.content_html = bbcode.parse(self.content)
        super(Article, self).save()


class Page(models.Model):
    title = models.CharField(max_length=120, primary_key=True)
    content = models.TextField()
    content_html = models.TextField(editable=False, blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self):
        self.content_html = bbcode.parse(self.content)
        super(Page, self).save()


class Comment(models.Model):
    title = models.CharField(max_length=120, primary_key=True)
    Article = models.ForeignKey(Article)
    content = models.TextField()
    author = models.CharField(max_length=60)
    authorEmail = models.EmailField()
    date = models.DateTimeField(auto_now_add=True, auto_now=True, verbose_name="Date de parution")

    def __str__(self):
        return self.title
