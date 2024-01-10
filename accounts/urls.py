from . import views
from django.urls import path

urlpatterns = [
path('register/', views.register,name='register'),
path('login/', views.login, name='login'),
path('logout/', views.logout, name='logout'),
path('dashboard/', views.dashboard, name='dashboard'),
path('', views.dashboard, name='dashboard'),
path('forgotPassword/',views.forgotPassword,name='forgotPassword'),
]