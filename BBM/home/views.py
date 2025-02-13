from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from B_Court.models import Court
from B_User.models import CourtManager, CourtStaff, Customer
from models import Staff 
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
            if Customer.objects.filter(account=user).exists():
                return redirect("role1")
            elif CourtManager.objects.filter(account=user).exists():
                return redirect("role3")
            elif CourtStaff.objects.filter(account=user).exists():
                return redirect("role2")
        else:
            return render(request, "home/login.html", {"error": "Tên đăng nhập hoặc mật khẩu không đúng"})
    return render(request, "home/login.html", {"user":request.user})

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
    # Logic cho view role3
    # return render(request, 'home/role3.html')

    courts = [
        {'name': 'Court 1', 'price': '100.000/h', 'location': '69, Nguyen Gia Trí, Phuong 25, Quan Binh Thanh', 'size': '5 san', 'capacity': '12 nguoi'},
        {'name': 'Court 2', 'price': '150.000/h', 'location': '456 Dien Bien Phu, Phuong 25, Quan Binh Thanh', 'size': '7 san', 'capacity': '15 nguoi'},
        # Thêm các sân khác ở đây
    ]
    employees = [
        {'name': 'A', 'position': 'Manager', 'email': 'A@gmail.com', 'phone': '123-456-7890'},
        {'name': 'B', 'position': 'Staff', 'email': 'B@gmail.com', 'phone': '098-765-4321'},
        # Thêm các nhân viên khác ở đây
    ]
    context = {
        'courts': courts,
        'employees': employees,
    }
    return render(request, 'home/role3.html', context)

def staffManage(request):
    staff =[
        {'ID': '01','Tên': 'Điểu Đinh', 'Số Điện Thoại':'0358493756', 'Email':'dieu@gmail.com','Trạng Thái':'Active','Chi tiết':'i'}
    ]
    context ={
        'staff':staff,
    }
    return render(request,'home/staffManage.html',context)