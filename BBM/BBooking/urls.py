from django.urls import path
from . import views

urlpatterns = [
    path('booking/<str:maCourt>/', views.booking, name='booking'),
    path('dateBooking/<str:maCourt>/<str:tp>/', views.dateBooking, name='dateBooking'),
    path('fixedBooking/<str:maCourt>/<str:tp>/', views.fixedBooking, name='fixedBooking'),
    path('flexBooking/<str:maCourt>/', views.flexBooking, name='flexBooking'),
    path('voucher/<str:maCourt>/<str:tp>/<str:ts>/<str:d>/<str:s>/', views.voucher, name='voucher'),
    path('tongtien/<str:maCourt>/<str:tp>/<str:ts>/<str:d>/<str:s>/<int:tien>/', views.TongTien, name='tongtien'),
    path('successBooking/<str:maCourt>/', views.successBooking, name='successBooking'),
]