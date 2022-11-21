from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import Student
from .serializer import stu_ser


# Create your views here.


class stu_view(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = stu_ser
    permission_classes =[permissions.AllowAny]
