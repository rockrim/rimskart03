from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('products_list/',views.products_list, name='products_list'),
    path('products_detail/<pk>', views.products_detail, name='products_detail'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)