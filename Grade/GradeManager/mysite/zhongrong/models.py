from django.db import models

# Create your models here.

class Grade(models.Model):
    classname = models.CharField(max_length=200)
    number = models.IntegerField(max_length=200)
