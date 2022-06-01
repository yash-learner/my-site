from django.shortcuts import render
from itsdangerous import Serializer
from rest_framework import viewsets
from .models import StudentApi
from .serializers import StudentApiSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api import serializers

# Create your views here.
@api_view(['GET', 'POST'])
def list_students(request):
  if request.method == 'GET':
    students = StudentApi.objects.all()
    Serializer = StudentApiSerializer(students, many = True)
    return Response(Serializer.data)
  elif request.method == 'POST':
    print(request.data)
    serializer = StudentApiSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def list_student(request, pk):
  if request.method == 'GET':
    student = StudentApi.objects.get(id=pk)
    serializer = StudentApiSerializer(student, many = False)
    return Response(serializer.data)
  elif request.method == 'PUT':
    student = StudentApi.objects.get(id=pk)
    serializer = StudentApiSerializer(student, data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
    student = StudentApi.objects.get(id=pk)
    student.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
