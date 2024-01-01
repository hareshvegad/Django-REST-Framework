from .models import Student
from .serializers import StudentSerializers
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [AllowAny]
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]