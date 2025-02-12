from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from app.models import Customer
from app.models import Manager
from app.models import Staff
from app.models import Court
from app.models import ListAccount
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

def list_staff(request):
    staff=Staff.objects.all()
    template=loader.get_template('home/list-staff.html')
    context={
        'staff':staff,
    }
    return HttpResponse(template.render(context,request))

def list_court(request):
    court=Court.objects.all()
    template=loader.get_template('home/list-court.html')
    context={
        'court': court,
    }
    return HttpResponse(template.render(context,request))

def list_account(request):
    account=ListAccount.objects.all()
    template=loader.get_template('home/list-account.html')
    context={
        'account': account,
    }
    return HttpResponse(template.render(context,request))

    



