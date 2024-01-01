from .models import Student
from .serializers import StudentSerializers
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status


class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({'message': 'Data created successfully', 'status_code': 1000}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Data creation failed', 'status_code': 999, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response({'message': 'Data updated successfully', 'status_code': 1000})
        else:
            return Response({'message': 'Data update failed', 'status_code': 999, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Data deleted successfully', 'status_code': 1000}, status=status.HTTP_204_NO_CONTENT)