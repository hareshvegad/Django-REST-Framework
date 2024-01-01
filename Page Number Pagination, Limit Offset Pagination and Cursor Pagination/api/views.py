from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student
# from .mypagination import MyPageNumberPagination 
# from .mypagination import MyLimitOffserPagination
from .mypagination import MyCursorPagination


# Create your views here.

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    # pagination_class = MyPageNumberPagination
    
    # pagination_class = MyLimitOffserPagination
    
    pagination_class = MyCursorPagination
    