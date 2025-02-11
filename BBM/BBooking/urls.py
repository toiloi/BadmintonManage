from django.urls import path
from . import views

urlpatterns = [
    path('BBooking/', views.HoaDon, name='hoadon'),
    path('BBooking/', views.VeDatSan, name='vedatsan'),
    path('BBooking/', views.TimeSlot, name='timeslot'),
]