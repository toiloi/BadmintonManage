from django.urls import path
from . import views

urlpatterns = [
    path('BBooking/', views.HoaDon, name='hoadon'),
    path('BBooking/', views.VeDatSan1, name='vedatsan'),
    path('BBooking/', views.TimeSlot, name='timeslot'),
    # path('confirm',VeDatSan1,name='confirm')
]