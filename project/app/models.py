from django.db import models

# Create your models here.


class Card(models.Model):
    title = models.CharField(max_length=200)
    des = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    rs= models.CharField(max_length=200)