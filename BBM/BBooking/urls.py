from django.urls import path
from . import views

urlpatterns = [
    path('booking/<str:maCourt>/', views.booking, name='booking'),
    path('dateBooking/<str:maCourt>/<str:tp>/', views.dateBooking, name='dateBooking'),
    path('fixedBooking/<str:maCourt>/<str:tp>/', views.fixedBooking, name='fixedBooking'),
    path('flexBooking/<str:maCourt>/<str:tp>/', views.flexBooking, name='flexBooking'),
    path('themgio/<str:maCourt>/<str:tp>/', views.themGio, name='themgio'),
    path('themlich/<str:maCourt>/<str:tp>/', views.themLich, name='themlich'),
    path('voucher/<str:maCourt>/<str:tp>/<str:ts>/<str:d>/<str:s>/', views.voucher, name='voucher'),
    path('tongtien/<str:maCourt>/<str:tp>/<str:ts>/<str:d>/<str:s>/<int:tien>/', views.TongTien, name='tongtien'),
    path('voucher1/<str:maCourt>/<str:tp>/<int:time>/', views.voucher1, name='voucher1'),
    path('tongtien1/<str:maCourt>/<str:tp>/<int:time>/<int:tien>/', views.TongTien1, name='tongtien1'),
    path('successBooking/<str:maCourt>/', views.successBooking, name='successBooking'),
]