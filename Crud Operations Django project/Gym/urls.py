from django.urls import path
from . import views

urlpatterns = [
    path('', views.Gym1, name='home'),
    path('service/', views.service_view, name='service'),
    path('about/', views.gym_about, name='about'),
    path('contact/', views.gym_contact, name='contact'),
]
