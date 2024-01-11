#from django.urls import path
#from . import views

#urlpatterns = [
  #  path('', views.cart, name='cart'),
   # path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    #path('checkout/', views.checkout, name='checkout'),
    #path('checkout/payments.html/', views.payments, name='payments'),  # URL pour la page de paiement
    #path('checkout/payments.html/', views.place_order, name='place_order'),  # Redirigez vers payments.html
    #path('remove_cart/<int:product_id>/', views.remove_cart_item, name='remove_cart'),
#]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('checkout/', views.checkout,name='checkout'),
path('remove_cart_item/<int:product_id>/', views.remove_cart_item, name='remove_cart_item'),
path('remove_cart/<int:product_id>/', views.remove_cart_item, name='remove_cart'),  # Rename this to 'remove_cart'

]
