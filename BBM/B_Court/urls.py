from django.urls import path
from . import views

urlpatterns = [
    path('B_Court/', views.Court, name='court'),
    path('B_Court/', views.San, name='san'),
]