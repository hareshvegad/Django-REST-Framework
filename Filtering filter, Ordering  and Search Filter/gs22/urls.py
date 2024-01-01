from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('StudentAPI/',views.StudentList.as_view(),name='studentlist')
]
