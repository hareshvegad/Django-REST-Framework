from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentAPI/',views.ListAndCreateStudentAPI.as_view(), name='student_api'),
    path('studentAPI/<int:pk>/',views.RetriveUpdateAndDestroyStudent.as_view(), name='student_api'),
]
