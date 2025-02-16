from django.urls import path
from . import views

urlpatterns = [
    path('BUser/', views.CourtStaff, name='courtstaff'),
    path('BUser/', views.User, name='User'),
    path('changeinf/', views.ChangeInf, name='changeinf'),
]