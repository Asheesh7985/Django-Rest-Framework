from django.shortcuts import render
from rest_framework.mixins import RetrieveModelMixin,UpdateModelMixin
from rest_framework.generics import GenericAPIView
from .models import Employee
from .serializers import EmployeeSerializer


class SingleEmployeeView(RetrieveModelMixin, GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)



class UpdateEmployee(UpdateModelMixin, GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)