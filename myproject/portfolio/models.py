from django.db import models
from django.utils import timezone
class Book(models.Model):
    title=models.CharField(max_length=100,unique=True)
    published_date=models.DateField()
    pages=models.IntegerField(default=0,null=False)
    description=models.TextField(blank=True)
    author=models.CharField(max_length=100,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    rating=models.DecimalField(max_digits=10,decimal_places=2,null=True)
class Post(models.Model):
    title=models.CharField(max_length=150,unique=True)
    subtitle=models.TextField(blank=True)
    author=models.CharField(max_length=150,blank=True)
    text=models.TextField(blank=True)
    published_date=models.DateTimeField(default=timezone.now)
    