
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('loadpage1/',views.loadpage1),
    path('sub1/',views.sub1),
    path('sub2/',views.sub2),
    path('sub3',views.sub3),
    path('sub4',views.sub4)
]