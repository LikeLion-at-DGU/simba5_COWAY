from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    attendance = models.PositiveIntegerField(default=0)

class Info(models.Model):
    latitude = models.DecimalField(max_digits=25, decimal_places=20)
    longitude = models.DecimalField(max_digits=25, decimal_places=20)
    name = models.CharField(max_length=30, null=False, blank=False)
    floor = models.TextField(blank=True)
    depart = models.BooleanField(default=False)
    image = models.ImageField(blank=True)
    near = models.TextField()

class conv(models.Model):
    latitude = models.DecimalField(max_digits=25, decimal_places=20)
    longitude = models.DecimalField(max_digits=25, decimal_places=20)
    name = models.CharField(max_length=30, null=False, blank=False)
    image = models.ImageField(blank=True)
    where = models.TextField()
    time = models.TextField()
    menu = models.TextField(blank=True)

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:30]