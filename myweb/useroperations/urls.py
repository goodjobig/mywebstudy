from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.acc_login, name='login'),
    path('logout/', views.acc_logout, name='logout'),
    path('register/', views.acc_register, name='register'),
]
