from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('changeinf/', views.ChangeInf, name='changeinf'),
    path('userdetail/', views.userDetail, name='userdetail'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='home/changepas.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='home/changepasdone.html'), name='password_change_done'),
]