from .models import Student
from .serializers import StudentSerializers
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    
    authentication_classes = [SessionAuthentication]
    
    # permission_classes = [IsAuthenticated]
    
    # permission_classes = [AllowAny]
    
    # permission_classes = [IsAdminUser]
    
    # permission_classes = [IsAuthenticatedOrReadOnly]
    
    # permission_classes = [DjangoModelPermissions]
    
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    