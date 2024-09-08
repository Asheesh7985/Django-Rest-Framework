from django.shortcuts import render
from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer
from restApp.customauth import CustomAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny, IsAuthenticatedOrReadOnly,IsAdminUser



class EmployeeAPIView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]
   
