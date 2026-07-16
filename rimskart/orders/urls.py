from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('orders/',views.show_cart, name='show_cart'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
