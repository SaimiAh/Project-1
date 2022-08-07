from pyexpat import model
from django.db import models
from tables import Description

class product(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class offer(models.Model):
    code= models.CharField(max_length=10)
    description= models.CharField(max_length=255)
    discount= models.FloatField()