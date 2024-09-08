from django.shortcuts import render
from rest_framework.mixins import RetrieveModelMixin,UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import GenericAPIView
from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeDelete(DestroyModelMixin, GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def delete(self,request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


