from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('role1', views.role1, name='role1'),
    path('role2', views.role2, name='role2'),
    path('role3', views.role3, name='role3'),
]