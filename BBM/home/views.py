from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from BCourt.models import Court
from BUser.models import CourtStaff, User
from django.contrib.auth.forms import UserCreationForm
from .models import RegisterForm

def home(request):
    return render(request, 'home/home.html')

def user_register(request):
    form = RegisterForm()
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "home/register.html", {'form':form})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            role = getattr(user, "role", None)  # Lấy role an toàn

            # Kiểm tra role và chuyển hướng phù hợp
            if role == "customer":
                return redirect("role1")  # Đường dẫn cho Customer
            elif role == "courtstaff":
                return redirect("role2")  # Đường dẫn cho CourtStaff
            elif role == "courtmanager":
                return redirect("role3")  # Đường dẫn cho CourtManager
            else:
                return render(request, "home/login.html", {"error": "Không xác định được vai trò của bạn."})

        return render(request, "home/login.html", {"error": "Tên đăng nhập hoặc mật khẩu không đúng."})

    return render(request, "home/login.html")

def user_logout(request):
    logout(request)
    return redirect("home")

# @login_required (login_url="login")
def role1(request):
    lc = Court.objects.all()
    return render(request, 'home/role1.html', {"lc":lc})

def role2(request):
    return render(request, 'home/role2.html')

def role3(request):
    return render(request, 'home/role3.html')

