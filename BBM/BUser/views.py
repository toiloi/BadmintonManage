from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

def CourtStaff(request):
    return HttpResponse("Hello world!")

def User(request):
    return HttpResponse("Hello world!")

def ChangeInf(request):
    user = request.user
    if request.method == "POST":
        form=UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()    
    return render(request, "")

