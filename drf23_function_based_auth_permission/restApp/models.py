from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=70)
    desg  = models.CharField(max_length=70)
    salary = models.IntegerField()

    def __str__(self):
        return self.name
