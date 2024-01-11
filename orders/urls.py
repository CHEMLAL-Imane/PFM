from django.urls import path
from . import views

urlpatterns = [
    path('payments.html/', views.place_order, name='place_order'),
    path('payments/<str:order_number>/', views.payment, name='payments'),
]
