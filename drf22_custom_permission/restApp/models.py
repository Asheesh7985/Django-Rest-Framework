from django.db import models

class Employee(models.Model):
    emp_name = models.CharField(max_length=70)
    emp_email = models.EmailField()
    emp_desgination = models.CharField(max_length=70)
    emp_salary = models.IntegerField()

    def __str__(self):
        return self.emp_name