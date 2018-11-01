"""paperproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from paperapp import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', views.index, name = 'index'),
    path('paper/', include('paperapp.urls')),
    path('admin/', admin.site.urls),
    path('register/', views.form_register, name = 'register'),
    path('logout/', views.form_logout, name= 'logout'),
    path('login/', views.form_login, name = 'login')
]
