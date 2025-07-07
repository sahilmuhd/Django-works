from django.db import models

# Create your models here.

class Dictionary(models.Model):
    word_entry = models.CharField(100)
    word_meaning = models.CharField(100)
