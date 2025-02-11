from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home/home.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password) 
        
        if user is not None:
            login(request, user)
            return redirect("role1")
        else:
            return render(request, "home/login.html", {"error": "Tên đăng nhập hoặc mật khẩu không đúng"})
    
    return render(request, "home/login.html", {"user":request.user})

def user_logout(request):
    logout(request)
    return redirect("home")

@login_required (login_url="login")
def role1(request):
     return render(request, 'home/role1.html')

def role2(request):
     return render(request, 'home/role2.html')

def role3(request):
     return render(request, 'home/role3.html')

