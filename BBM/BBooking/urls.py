from django.urls import path
from . import views

urlpatterns = [
    path('booking/<str:maCourt>/', views.booking, name='booking'),
    path('dailyBooking/<str:maCourt>/', views.dailyBooking, name='dailyBooking'),
]