from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=225)
    price=models.FloatField()
    stock=models.IntegerField()
    image=models.CharField(max_length=2500)

class Offer(models.Model):
    code=models.CharField(max_length=16)
    descrption= models.CharField(max_length=255)
    discount=models.FloatField()