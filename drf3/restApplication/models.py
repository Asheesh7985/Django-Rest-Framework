from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_name = models.CharField(max_length=70)
    employee_email = models.EmailField()
    employee_desgination = models.CharField(max_length=70)
    employee_salary = models.IntegerField()
