from django.db import models

# Create your models here.

class course(models.Model):
    code = models.CharField(max_length=12,primary_key=True)
    desc = models.CharField(max_length=50)

class Mentor(models.Model):
    id = models.CharField(max_length=5,primary_key=True)
    name = models.CharField(max_length=30)
    room = models.CharField(max_length=10)
