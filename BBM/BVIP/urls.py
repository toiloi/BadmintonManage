from django.urls import path
from . import views

urlpatterns = [
    path('BVIP/', views.VIP, name='vip'),
]