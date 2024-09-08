from django.shortcuts import render
from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny, IsAuthenticatedOrReadOnly,IsAdminUser



class EmployeeAPIView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]
    #permission_classes = [AllowAny]
    #permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [IsAdminUser]
