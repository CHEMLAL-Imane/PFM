from django.contrib import admin
from django.urls import path, include

# from .views import products_by_category

from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  
    path('store/', include('store.urls')),  
    path('cart/', include('carts.urls')),
    path('accounts/', include('accounts.urls')),
    path('orders/', include('orders.urls')),

    # path('products/<slug:category_slug>/', products_by_category, name='products_by_category'),

]

# Configuration pour servir les fichiers médias pendant le développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
