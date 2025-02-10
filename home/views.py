from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from app.models import Customer
from app.models import Manager
# Create your views here.
def home(request):
    return render(request,'home/home.html')

def customers(request):
    customers=Customer.objects.all()
    template=loader.get_template('home/customers.html')
    context={
        'customer': customers,
    }
    return HttpResponse(template.render(context,request))

def edit_customer(request):
    customer=Customer.objects.get(id = 1)
    template=loader.get_template('home/customer-edit.html')
    context={
        'customer': customer,
    }
    return HttpResponse(template.render(context,request))

def court_manager(request):
    manager=Manager.objects.all()
    template=loader.get_template('home/court-manager.html')
    context={
        'manager':manager,
    }
    return HttpResponse(template.render(context,request))

    



