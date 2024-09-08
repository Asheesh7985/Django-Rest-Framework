from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=70)
    desgination = models.CharField(max_length=70)
    salary = models.IntegerField()

