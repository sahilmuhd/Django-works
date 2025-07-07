from django.db import models

# Create your models here.

class Contacts(models.Model):
    name = models.CharField(100)
    email = models.CharField(100)
    number = models.BigIntegerField()
    address = models.CharField(255)

