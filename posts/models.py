from django.db import models
from django.utils import timezone
import datetime

class Product(models.Model):
    title=models.CharField(max_length=255)
    price=models.CharField(max_length=50)
    image=models.TextField()
    mrp=models.CharField(max_length=50)
    saving=models.CharField(max_length=50)
    url=models.TextField(max_length=100)
    date=models.DateTimeField(default=datetime.date.today,max_length=50)
