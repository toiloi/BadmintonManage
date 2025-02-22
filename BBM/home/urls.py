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
    
    path('r3confirm',views.Confirm,name='r3confirm'),
    path('r3vip',views.Vip,name='r3vip'),
    path('r3voucher',views.Voucher,name='r3voucher'),
    path('delete-voucher/<str:voucher>/',views.delete_voucher,name='delete-voucher'),
    path('r3liststaff',views.list_nhanvien,name='r3liststaff'),
    path('r3listxv',views.list_xinviec,name='r3listxv'),
    path('r3duyet/<str:court>/<str:staff>/<str:action>',views.duyetDon,name='r3duyet'),
]