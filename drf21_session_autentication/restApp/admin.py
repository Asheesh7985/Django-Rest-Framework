from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','emp_name','emp_email','emp_desgination','emp_salary']
