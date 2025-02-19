from django.urls import path
from . import views

urlpatterns = [
    path('booking/<str:maCourt>/', views.booking, name='booking'),
    path('dateBooking/<str:maCourt>/', views.dateBooking, name='dateBooking'),
    path('voucher/<str:maCourt>/<str:ts>/<str:d>/<str:s>/', views.voucher, name='voucher'),
    path('tongtien/<str:maCourt>/<int:flagid>/', views.tongTien, name='tongtien'),
]