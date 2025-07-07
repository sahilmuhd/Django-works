from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
    path('product1/',views.product1),
    path('product2/',views.product2),
    path('product3/',views.product3),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),
    path('edit/<int:id>/', views.edit_product, name='edit_product'),
    path('update/<int:id>/',views.update_product, name='update_product'),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('view-cart/', views.view_cart, name='view_cart'),
    path('checkout/',views.check_out,name='checkout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
