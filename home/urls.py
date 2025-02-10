from django.contrib import admin # type: ignore
from django.urls import include,path # type: ignore
from .import views

urlpatterns = [
    path('', views.home, name= "home"),
    path('customers',views.customers,name="customers"),
    path('edit-customer',views.edit_customer,name="edit-customer"),
    path('court-manager',views.court_manager,name="court-manager")
]