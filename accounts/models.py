from django.db import models

class Account(models.Model):
    fullname=models.CharField(max_length=32)
    username=models.CharField(max_length=100)
    date=models.DateTimeField()
    password=models.CharField(max_length=32)

class Cart(models.Model):
    username=models.CharField(max_length=100)
    pid=models.IntegerField()
