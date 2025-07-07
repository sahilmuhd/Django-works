from django.urls import path
from . import views
urlpatterns = [
    path('dictionary/',views.enter),
    path('dictionary2/',views.enter2),
    path('enter3/',views.enter3)
    ]