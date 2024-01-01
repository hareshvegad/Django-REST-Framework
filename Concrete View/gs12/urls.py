from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('studentAPI/',views.StudentList.as_view(), name='student_api'),
    # path('studentAPI/',views.StudentCreate.as_view(), name='student_api'),
    # path('studentAPI/<int:pk>/',views.StudentRetrieve.as_view(), name='student_api'),
    # path('studentAPI/<int:pk>/',views.StudentUpdate.as_view(), name='student_api'),
    # path('studentAPI/<int:pk>/',views.StudentDestroy.as_view(), name='student_api'),
    
    
    
    # path('studentAPI/',views.StudentListCreate.as_view(), name='student_api'),
    # path('studentAPI/<int:pk>/',views.StudentRetrieveUpdate.as_view(), name='student_api'),
    # path('studentAPI/<int:pk>/',views.StudentRetrieveDestroy.as_view(), name='student_api'),
    # path('studentAPI/<int:pk>/',views.StudentRetrieveUpdateDestroy.as_view(), name='student_api'),
    
    
    
    #CRUD
    path('studentAPI/',views.StudentListCreate.as_view(), name='student_api'),
    path('studentAPI/<int:pk>/',views.StudentRetrieveUpdateDestroy.as_view(), name='student_api'),
]
