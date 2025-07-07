from django.db import models

# Create your models here.

class employee(models.Model):
    name = models.CharField(100)
    email = models.CharField(100)
    address = models.CharField(200)
    number = models.IntegerField(100)
