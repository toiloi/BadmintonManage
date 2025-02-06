from django.urls import path
from . import views

urlpatterns = [
    path('B_VIP/', views.VIP, name='vip'),
]