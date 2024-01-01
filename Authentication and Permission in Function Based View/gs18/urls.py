from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentAPI/',views.student_api, name='student_api'),
    path('studentAPI/<int:pk>/',views.student_api, name='student_api'),
]
