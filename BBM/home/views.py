from django.shortcuts import render, redirect
from django.http import HttpResponse
from B_User.models import Account
from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home/home.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if Account.objects.filter(useName=username).exists():
            user = Account.objects.get(useName = username)
            pw = user.password
            if password == pw:
                return redirect("role1")
            else:
                return render(request, "home/login.html", {"error": "Tên đăng nhập hoặc mật khẩu không đúng"})
        else:
            return render(request, "home/login.html", {"error": "Tên đăng nhập hoặc mật khẩu không đúng"})
    return render(request, "home/login.html")

# @login_required
def role1(request):
     return render(request, 'home/role1.html')

