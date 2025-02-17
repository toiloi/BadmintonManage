from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from BCourt.models import Court, Sonha, Duong, Phuong, Quan, Tinh
from BUser.models import CourtStaff, User
from django.contrib.auth.forms import UserCreationForm
from .forms import CourtForm, AddressForm
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

@login_required(login_url="login")
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

@login_required(login_url="login")
def add_court(request):
    managers = User.objects.filter(role='courtmanager')
    if request.method == 'POST':
        court_form = CourtForm(request.POST, request.FILES)
        address_form = AddressForm(request.POST)
        if court_form.is_valid() and address_form.is_valid():
            court = court_form.save(commit=False)
            address = address_form.cleaned_data['tinh']
            court.address = address
            court.save()
            return redirect('manage_court')
    else:
        court_form = CourtForm()
        address_form = AddressForm()
    return render(request, "home/add_court.html", {'court_form': court_form, 'address_form': address_form, 'managers': managers})

@login_required(login_url="login")
def manage_court(request):
    courts = Court.objects.all()
    return render(request, "home/manage_courts.html", {'courts': courts})

@login_required(login_url="login")
def delete_court(request, court_id):
    court = get_object_or_404(Court, id=court_id)
    if request.method == 'POST':
        court.delete()
        return redirect('manage_court')
    return render(request, "home/manage_courts.html", {'courts': Court.objects.all()})

@login_required(login_url="login")
def time_slot(request):
    return render(request, "home/time_slot.html")

@login_required(login_url="login")
def pricing(request):
    return render(request, "home/pricing.html")

@login_required(login_url="login")
def policy(request):
    return render(request, "home/policy.html")

@login_required(login_url="login")
def load_add_court(request):
    return render(request, "home/add_court.html")

@login_required(login_url="login")
def load_manage_court(request):
    courts = Court.objects.all()
    return render(request, "home/manage_courts.html", {'courts': courts})

@login_required(login_url="login")
def load_time_slot(request):
    return render(request, "home/time_slot.html")

@login_required(login_url="login")
def load_pricing(request):
    return render(request, "home/pricing.html")

@login_required(login_url="login")
def load_policy(request):
    return render(request, "home/policy.html")

