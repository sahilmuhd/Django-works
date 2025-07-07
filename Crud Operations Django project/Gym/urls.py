from django.urls import path
from . import views
urlpatterns = [
    path('Gym/',views.Gym1),
    path('gym2/',views.Gym2),
    ]


