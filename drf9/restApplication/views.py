from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import student
from .serializers import StudentSerializer


@api_view(['GET','POST','PUT','PATCH','DELETE'])
def StudentAPIView(request):
    if request.method == 'GET':
        id = request.data.get('id')
        print(id)
        if id is not None:
            stu = student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Created'}
            return Response(res)
        return Response(serializer.error)
    
    if request.method == 'PUT':
        id = request.data.get('id')
        stu = student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated Successfully!!!'})
        return Response(serializer.errors)
    
    if request.method == 'PATCH':
        id = request.data.get('id')
        stu = student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated Successfully!!!'})
        return Response(serializer.errors)
    

    if request.method == "DELETE":
        id = request.data.get('id')
        stu = student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted  Successfully!!!'})



    
    

