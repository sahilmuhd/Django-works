
from django.urls import path
from . import views
urlpatterns = [
    path('',views.crud),
    path('contactentry/',views.contactentry),
    path('deletecontact/<int:id>',views.deletecontact,name='deletecontact'),
    path('editcontact/<int:id>',views.editcontact,name="editcontact"),
    path('updatecontact/',views.updatecontact,name='updatecontact'),
]


