"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import rest_framework_simplejwt.views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/account/', include('djoser.urls')),
    path('api/v1/auth/login/', jwt_views.TokenObtainPairView.as_view(), name='auth'),
    path('api/v1/auth/verify/', jwt_views.TokenVerifyView.as_view(), name='verify'),
    path('api/v1/auth/refresh/', jwt_views.TokenRefreshView.as_view(), name='refresh'),
    path('api/v1/app/', include("app.urls")),
    path('', include("frontend.urls")),
]
