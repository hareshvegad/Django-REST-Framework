from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

# Create Router Object
router = DefaultRouter()

# Register StudentViewSet With Router
router.register('studentAPI', views.StudentViewSet, basename="student")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/',include('rest_framework.urls'),name='rest_framework'),
    
    path('studentapi/',views.StudentList.as_view()),
    path('studentapi/',views.StudentCreate.as_view()),    
    path('studentapi/<int:pk>/',views.StudentRetrieve.as_view()),
    path('studentapi/<int:pk>/',views.StudentUpdate.as_view()),
    path('studentapi/<int:pk>/',views.StudentDestroy.as_view()),
]
