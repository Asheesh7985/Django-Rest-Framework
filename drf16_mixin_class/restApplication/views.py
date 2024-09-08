from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin,ListModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import GenericAPIView
from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeCreate(CreateModelMixin, GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class AllEmployee(ListModelMixin, GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    

class SingleEmployee(RetrieveModelMixin, GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
class SingleUpdateEmployee(UpdateModelMixin, GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class DeleteEmployee(DestroyModelMixin, GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)






