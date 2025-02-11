from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from BCourt.models import Court
from BUser.models import CourtStaff, User

def home(request):
    return render(request, 'home/home.html')

def user_register(request):
    return render(request, "register.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password) 
        
        if user is not None:
            login(request, user)

            # Kiểm tra role và chuyển hướng phù hợp
            if hasattr(user, "customer"):
                return redirect("role1")  # Đường dẫn cho Customer
            elif hasattr(user, "courtstaff"):
                return redirect("role2")  # Đường dẫn cho CourtStaff
            elif hasattr(user, "courtmanager"):
                return redirect("role3")  # Đường dẫn cho CourtManager
        else:
            return render(request, "home/login.html", {"error": "Tên đăng nhập hoặc mật khẩu không đúng"})
    
    return render(request, "home/login.html", {"user": request.user})

def user_logout(request):
    logout(request)
    return redirect("home")

@login_required (login_url="login")
def role1(request):
    lc = Court.objects.all()
    return render(request, 'home/role1.html', {"lc":lc})

def role2(request):
    return render(request, 'home/role2.html')

def role3(request):
    return render(request, 'home/role3.html')

