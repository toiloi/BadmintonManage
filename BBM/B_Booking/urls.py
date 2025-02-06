from django.urls import path
from . import views

urlpatterns = [
    path('B_Booking/', views.HoaDon, name='hoadon'),
    path('B_Booking/', views.VeDatSan, name='vedatsan'),
    path('B_Booking/', views.TimeSlot, name='timeslot'),
]