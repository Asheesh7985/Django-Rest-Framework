from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
