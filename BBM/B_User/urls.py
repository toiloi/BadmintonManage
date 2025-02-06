from django.urls import path
from . import views

urlpatterns = [
    path('B_User/', views.Account, name='account'),
    path('B_User/', views.CourtStaff, name='courtstaff'),
    path('B_User/', views.CourtManager, name='courtmanager'),
    path('B_User/', views.Position, name='position'),
    path('B_User/', views.Customer, name='customer'),
]