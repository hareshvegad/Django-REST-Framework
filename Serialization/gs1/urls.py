from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.student_detail, name="student_detail"),
    path('', views.student_detail, name="student_detail"),
    path('student/<int:pk>/', views.student_detail, name="student_detail"),
    path('student_info/', views.student_list, name="student_detail"),
]
