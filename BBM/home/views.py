from django.shortcuts import render, redirect, get_object_or_404
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
    
def datSan(request):
    return render(request, "home/datsan.html")

def chiTiet(request, maCourt):
    court = get_object_or_404(Court, maCourt = maCourt)
    return render(request, "home/detail.html", {"court":court})

def xetduyetNhanVien(request):
    return render(request, "home/xetduyetNhanVien.html")

def staffList(request):
    return render(request, "home/staffList.html")

def ChamCong(request):
    return render(request, "home/chamCong.html")

def payment(request):
    return render(request, "home/payment.html")

def Revenue(request):
    return render(request, "home/Revenue.html")

<<<<<<< HEAD
=======
def role3(request):
    # Logic cho view role3
    # return render(request, 'home/role3.html')
>>>>>>> 81997368de2b5ecf98fbd5d5df94dfa39d0fd36d

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