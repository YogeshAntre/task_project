from django.db import models

# Create your models here.

class Item(models.Model):
    name=models.CharField(max_length=40,unique=True)
    desc=models.TextField(max_length=100)
    qty=models.IntegerField()