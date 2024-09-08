from django.shortcuts import render
from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET','POST','PUT','PATCH','DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def EmployeeApiView(request, pk=None):
    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'})
        return Response(serializer.errors)

    if request.method == 'GET':
        id = pk
        if id is not None:
            stu = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(stu)
            return Response(serializer.data)
        stu = Employee.objects.all()
        serializer = EmployeeSerializer(stu, many=True)
        return Response(serializer.data)

    if request.method == 'PUT':
        id=pk
        stu = Employee.objects.get(pk=id)
        serializer = EmployeeSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated Successfully'})
        return Response({'msg':'Data updated Successfully'})

    if request.method == 'PATCH':
        id=pk
        stu = Employee.objects.get(pk=id)
        serializer = EmployeeSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated Successfully'})
        return Response({'msg':'Data updated Successfully'})


    if request.method == 'DELETE':
        id = pk
        stu = Employee.objects.get(pk=id)
        stu.delete
        return Response({'msg':'Data Deleted Successfully'})

