from django.shortcuts import render
from rest_framework.mixins import ListModelMixin
from rest_framework.generics import GenericAPIView
from .models import Employee
from .serializers import EmployeeSerializer

class StudentList(ListModelMixin, GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

