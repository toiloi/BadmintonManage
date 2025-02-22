from django.urls import path
from . import views

urlpatterns = [
    path('add-court/', views.add_court, name='r3add_court'),
    path('manage-court/', views.manage_court, name='r3manage_court'), 
    path('chi-tiet/<str:maCourt>/', views.chiTiet, name='chiTiet'),
    path('add_san/<str:maCourt>/', views.add_san, name='r3add_san'),
    path('delete-court/<str:maCourt>/', views.delete_court, name='delete_court'), 
    path('delete-san/<str:maSan>/', views.delete_san, name='delete_san'),
]