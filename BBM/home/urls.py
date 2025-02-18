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
    path('detail/<str:maCourt>/', views.chiTiet, name='detail'),
]