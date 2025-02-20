from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('changeinf/', views.ChangeInf, name='changeinf'),
    path('changeinf2/', views.ChangeInf2, name='changeinf2'),
    path('userdetail/', views.userDetail, name='userdetail'),
    path('userdetail2/', views.userDetail2, name='userdetail2'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='home/changepas.html'), name='password_change'),
    path('password_change2/', auth_views.PasswordChangeView.as_view(template_name='home/changepas2.html'), name='password_change2'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='home/changepasdone.html'), name='password_change_done'),
]