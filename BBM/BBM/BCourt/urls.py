from django.urls import path
from . import views

urlpatterns = [
    path('BCourt/', views.Court, name='court'),
    path('BCourt/', views.San, name='san'),
]