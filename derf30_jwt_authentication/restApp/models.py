from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()
    city = models.CharField(max_length=70)
