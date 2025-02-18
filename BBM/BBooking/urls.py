from django.urls import path
from . import views

urlpatterns = [
    path('datsan/<str:maCourt>/', views.datSan, name='datsan'),
]