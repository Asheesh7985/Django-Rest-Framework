from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.Serializer):
    employee_name = serializers.CharField(max_length=70)
    employee_email = serializers.EmailField()
    employee_desgination = serializers.CharField(max_length=70)
    employee_salary = serializers.IntegerField()

    def create(self, validate_data):
        return Employee.objects.create(**validate_data)