from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin
from rest_framework.generics import GenericAPIView
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeCreateView(CreateModelMixin,GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    


