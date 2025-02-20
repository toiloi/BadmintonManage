from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('role/', views.role, name='role'),
    path('filter/', views.courtFilter, name='filter'),
    path('his/', views.history, name='his'),
    path('deleteHis/<str:maVe>/', views.deleteHistory, name='deleteHis'),
    path('detail/<str:maCourt>/', views.chiTiet, name='detail'),
    

    path('r2dangky/', views.r2dangky, name='r2dangky'),
    path('r2court/', views.r2court, name='r2court'),
    path('r2checkin/<str:maCourt>/', views.r2checkIn, name='r2checkin'),
    
    path('confirm',views.Confirm,name='confirm'),
    path('vip',views.Vip,name='vip'),
    path('voucher',views.Voucher,name='voucher')
]