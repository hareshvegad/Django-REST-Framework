from .models import Student
from .serializers import StudentSerializers
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.throttling import ScopedRateThrottle

from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from api.throttling import JackRateThottle

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]
    
    throttle_classes = [AnonRateThrottle, JackRateThottle]
    
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewstu'
    
class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'createstu'
    
class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewstu'
    
class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'createstu'
    
class StudentDestroy(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'createstu'