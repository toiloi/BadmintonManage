
from django.urls import path
from . import views
# from .views import role3, add_court, delete_court

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('role/', views.role, name='role'),
    path('datsan/', views.datSan, name='datsan'),
    path('add-court/', views.add_court, name='add_court'),
    path('manage-court/', views.manage_court, name='manage_court'),
    path('time-slot/', views.time_slot, name='time_slot'),
    path('pricing/', views.pricing, name='pricing'),
    path('policy/', views.policy, name='policy'),
    path('delete-court/<int:court_id>/', views.delete_court, name='delete_court'),
    path('load-add-court/', views.load_add_court, name='load_add_court'),
    path('load-manage-court/', views.load_manage_court, name='load_manage_court'),
    path('load-time-slot/', views.load_time_slot, name='load_time_slot'),
    path('load-pricing/', views.load_pricing, name='load_pricing'),
    path('load-policy/', views.load_policy, name='load_policy'),

    path('detail/<str:maCourt>/', views.chiTiet, name='detail'),
]


# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('login/', views.user_login, name='login'),
#     path('register/', views.user_register, name='register'),
#     path('logout/', views.user_logout, name='logout'),
#     path('role/', views.role, name='role'),
#     path('datsan/', views.datSan, name='datsan'),
#     path('add-court/', views.add_court, name='add_court'),
#     path('manage-court/', views.manage_court, name='manage_court'),
#     path('time-slot/', views.time_slot, name='time_slot'),
#     path('pricing/', views.pricing, name='pricing'),
#     path('policy/', views.policy, name='policy'),
#     path('delete-court/<int:court_id>/', views.delete_court, name='delete_court'),
# ]