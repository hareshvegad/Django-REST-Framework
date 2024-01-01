from .models import Student
from .serializers import StudentSerializers
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    
    authentication_classes = [TokenAuthentication]
    
    # permission_classes = [IsAuthenticated]
    
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    