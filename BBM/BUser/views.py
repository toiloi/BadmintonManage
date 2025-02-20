from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm

def userDetail(request):
    user=request.user
    return render(request, "home/userdetail.html", {'user':user})

def userDetail2(request):
    user=request.user
    return render(request, "home/r2userdetail.html", {'user':user})

def ChangeInf(request):
    user = request.user
    form=UserForm(request.POST, instance=user)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('userdetail')    
    return render(request, "home/useredit.html", {'form':form})

def ChangeInf2(request):
    user = request.user
    form=UserForm(request.POST, instance=user)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('userdetail')    
    return render(request, "home/r2useredit.html", {'form':form})