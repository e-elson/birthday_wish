from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Wish(models.Model):
    author = models.CharField(max_length=40)
    description = models.CharField(max_length=50)
    email = models.CharField(max_length=40)
    body = models.TextField(max_length=500)
    status = models.CharField(max_length=15, default="Not Published")
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author

class Reply(models.Model):
    msg = models.TextField(max_length=250)
    wish = models.ForeignKey(Wish, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.msg

class Gallery(models.Model):
    image = models.FilePathField(path='/images')
    desc = models.CharField(max_length=60)
    def __str__(self):
        return self.desc

class Image(models.Model):
    image = models.FilePathField(path='/images')
