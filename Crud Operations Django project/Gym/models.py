from django.db import models

# Create your models here.
class Gymdata(models.Model):  # ✅ Correct base class
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.name
