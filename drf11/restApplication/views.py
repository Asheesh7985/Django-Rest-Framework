from rest_framework.views import APIView
from .models import student
from .serializers import StudentSerializer
from rest_framework.response import Response

class StudentAPIView(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            stu  = student.objects.get(pk=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data created Successfully'}
            return Response(res)
        return Response(serializer.error)

    def put(self, request, pk, format=None):
        id = pk
        stu  = student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data updated Successfully'}
            return Response(res)
        return Response(serializer.error)
    

    def patch(self, request, pk, format=None):
        id = pk
        stu  = student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data updated Successfully'}
            return Response(res)
        return Response(serializer.error)

    def delete(self, request, pk, format=None):
        id=pk
        stu  = student.objects.get(pk=id)
        stu.delete()
        res = {'msg':'Data Deleted Successfully'}
        return Response(res)
       

        



