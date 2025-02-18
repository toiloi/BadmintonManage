from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from BCourt.models import Court,CourtStaff
from BUser.models import  User
from django.contrib.auth.forms import UserCreationForm
from .models import RegisterForm, Transaction, staffRequest, DailyStat

def home(request):
    return render(request, 'home/home.html')

def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Chuyển hướng sau khi đăng ký thành công
    else:
        form = RegisterForm()
    
    return render(request, "home/register.html", {'form': form})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            role = getattr(user, "role", None)  # Lấy role an toàn
            if role == "customer" or role == "courtstaff" or role == "courtmanager":
                return redirect("role")
            else:
                logout(request)
                return render(request, "home/login.html", {"error": "Không xác định được vai trò của bạn."})
        return render(request, "home/login.html", {"error": "Tên đăng nhập hoặc mật khẩu không đúng."})
    return render(request, "home/login.html")

def user_logout(request):
    logout(request)
    return redirect("home")

@login_required (login_url="login")
def role(request):
    user = request.user
    role = getattr(user, "role", None)
     # Kiểm tra role và chuyển hướng phù hợp
    if role == "customer":
        lc = Court.objects.all()
        return render(request, "home/role1.html", {"lc":lc})  # Đường dẫn cho Customer
    elif role == "courtstaff":
        return render(request, "home/role2.html")  # Đường dẫn cho CourtStaff
    elif role == "courtmanager":
        return render(request, "home/role3.html")  # Đường dẫn cho CourtManager
    else:
        return HttpResponse("Không xác định được vai trò của bạn.", status=400)
    
def datSan(request):
    return render(request, "home/datsan.html")

def chiTiet(request, maCourt):
    court = get_object_or_404(Court, maCourt = maCourt)
    return render(request, "home/detail.html", {"court":court})

def xetduyetNhanVien(request):
    return render(request, "home/xetduyetNhanVien.html")

def staffList(request):
    staff_list = CourtStaff.objects.all()
    return render(request, "home/staffList.html", {"staff_list": staff_list})

def ChamCong(request):
    staff_list = CourtStaff.objects.all()
    for staff in staff_list:
        staff.total_salary = staff.days_worked * staff.salary_per_day
    return render(request, "home/chamCong.html", {"staff_list": staff_list})

def payment(request):
    return render(request, "home/payment.html")

def Revenue(request):
    daily_stats = DailyStat.objects.all()
    total_revenue = sum(stat.revenue for stat in daily_stats)
    total_bookings = sum(stat.bookings for stat in daily_stats)
    return render(request, "home/Revenue.html", 
        {"daily_stats": daily_stats,
         "total_revenue": total_revenue, 
         "total_bookings": total_bookings
         })

