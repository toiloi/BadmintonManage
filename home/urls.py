from django.contrib import admin # type: ignore
from django.urls import include,path # type: ignore
from .import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name= "home"),
    path('customers',views.customers,name="customers"),
    path('edit-customer',views.edit_customer,name="edit-customer"),
    path('court-manager',views.court_manager,name="court-manager"),
    path('list-staff', views.list_staff,name='list-staff'),
    path('list-court',views.list_court,name='list-court'),
    path('list-account',views.list_account,name='list-account')
]