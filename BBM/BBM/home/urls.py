from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('role/', views.role, name='role'),
    path('datsan/', views.datSan, name='datsan'),
    path('detail/<str:maCourt>/', views.chiTiet, name='detail'),
    path('confirm',views.Confirm,name='confirm'),
    path('vip',views.Vip,name='vip'),
    path('voucher',views.Voucher,name='voucher')
]