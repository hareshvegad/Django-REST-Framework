from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from api.auth import CustomAuthToken

# Create Router Object
router = DefaultRouter()

# Register StudentViewSet With Router
router.register('studentAPI', views.StudentViewSet, basename="student")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/',include('rest_framework.urls'),name='rest_framework'),
    
    # Get Token from Server
    # path('gettoken/', obtain_auth_token),
    
    # Get Token from Server with auth.py
    path('gettoken/', CustomAuthToken.as_view()),
]
