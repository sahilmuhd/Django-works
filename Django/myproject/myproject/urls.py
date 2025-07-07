"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('login/',views.login),
    path('register/',views.register),
    path('logindata/',views.logindata),
    path('registerdata/',views.registerdata),
    path('sub1/',views.sub1),
    path('sub2/',views.sub2),
    path('sub3/',views.sub3),
    path('sub4/',views.sub4),
    path('list1/',views.list1),
    path('list2/',views.list2)
]
