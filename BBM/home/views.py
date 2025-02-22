from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from BUser.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import RegisterForm
from BCourt.models import Court, San, Rating, xinViec
from BBooking.models import VeDatSan
from django.urls import reverse
from BBooking.forms import Gangzbit
from BBooking.models import Voucher as Voucher_model
from django.db.models import Q


def home(request):
    return render(request, 'home/home.html')

def role_required(role):
    def check_role(user):
        return user.is_authenticated and user.role == role
    return user_passes_test(check_role, login_url="login")

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
# @role_required(["customer", "courtmanager", "courtstaff"])
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
    
def history(request):
    user=request.user
    lb = VeDatSan.objects.filter(customer=user)
    return render(request, 'home/history.html', {"lb":lb})

def deleteHistory(request, maVe):
    if request.method == 'POST':
        ve=get_object_or_404(VeDatSan, maVe=maVe)
        ve.flag.delete()
        return redirect('his')
    return render(request, 'home/deleteHistory.html', {"maVe":maVe})

def chiTiet(request, maCourt):
    court = get_object_or_404(Court, maCourt = maCourt)
    san=San.objects.filter(court=court).count()
    if request.method == "POST":
        user=request.user
        rate=request.POST.get("rating")
        check=Rating.objects.filter(customer=user,court=court).exists()
        if check:
            r=get_object_or_404(Rating,customer=user,court=court)
            r.rate=rate
            r.save()
        else:
            r=Rating.objects.create(
                customer=user,
                rate=rate,
                court=court
            )
        url = reverse("detail", kwargs={"maCourt": maCourt})
        return redirect(url)
    return render(request, "home/detail.html", {"court":court, "san":san})

def search(request):
    query = request.GET.get('q')  
    results = Court.objects.filter(name__icontains=query) if query else []  
    return render(request, "home/search.html", {'results': results, 'query': query})

def courtFilter(request):
    selected_price = request.GET.get("price", "")
    selected_tinh = request.GET.get("tinh", "")
    selected_quan = request.GET.get("quan", "")
    selected_phuong = request.GET.get("phuong", "")
    selected_duong = request.GET.get("duong", "")

    courts = Court.objects.all()

    # Lọc theo mức giá
    if selected_price == "low":
        courts = courts.filter(price__lt=50000)
    elif selected_price == "medium":
        courts = courts.filter(price__gte=50000, price__lte=100000)
    elif selected_price == "high":
        courts = courts.filter(price__gt=100000)

    # Lọc theo địa chỉ
    if selected_tinh:
        courts = courts.filter(address__tinh__icontains=selected_tinh)

    if selected_quan:
        courts = courts.filter(address__quan__icontains=selected_quan)

    if selected_phuong:
        courts = courts.filter(address__phuong__icontains=selected_phuong)

    if selected_duong:
        courts = courts.filter(address__duong__icontains=selected_duong)

    context = {
        "courts": courts,
    }

    return render(request, "home/filter.html", context)

def r2dangky(request):
    user=request.user
     # Danh sách các sân mà nhân viên đã gửi đơn nhưng chưa bị từ chối
    lc = Court.objects.exclude(
    xinviec__courtStaff=user, xinviec__duyet__in=["approved", "pending"]
    )
    if request.method == 'POST':
        maCourt=request.POST.get("maCourt") 
        court=get_object_or_404(Court,maCourt=maCourt) 
        check =xinViec.objects.filter(court=court, courtStaff=user).exists()
        if not check:
            xv=xinViec.objects.create(court=court, courtStaff=user)
    return render(request, "home/r2workRegister.html", {"lc":lc})

def list_nhanvien(request):
    ls = User.objects.filter(id__in=Court.objects.values_list("courtStaff", flat=True)).distinct()
    return render(request, "home/r3staffList-dinh.html", {"ls":ls})

def list_xinviec(request):
    user=request.user
    lx = xinViec.objects.filter(court__courtManager=user, duyet="pending")
    if request.method == 'POST':
        action = request.POST.get("action")
        c=request.POST.get("court")
        s=request.POST.get("staff")
        
        url = reverse("r3duyet", kwargs={"court": c, "staff":s, "action":action})
        return redirect(url)
    return render(request, "home/r3xetduyet-dinh.html", {"lx":lx})

def duyetDon(request, court, staff, action):
    staff=get_object_or_404(User, username=staff)
    court=get_object_or_404(Court, maCourt=court)
    don=get_object_or_404(xinViec, court=court,courtStaff=staff)
    if action == 'approve':
        don.duyet = 'approved'
        court.courtStaff.add(staff)
    else:
        don.duyet = 'rejected'
    don.save()
    return redirect('r3listxv')
    

def r2court(request):
    user=request.user 
    lc = Court.objects.filter(courtStaff=user)
    print (lc)
    return render(request, "home/r2court.html", {"lc":lc})

def r2checkIn(request, maCourt):
    court=get_object_or_404(Court,maCourt=maCourt)
    lve = VeDatSan.objects.filter(checkin='chuacheckin', flag__san__court=court)

    if request.method == 'POST':
        action = request.POST.get("action")  
        ma_ve = request.POST.get("maVe") 

        try:
            ve = VeDatSan.objects.get(maVe=ma_ve) 
            if action == "confirm":
                ve.checkin = "dacheckin"  
                ve.save()
            elif action == "cancel":
                ve.flag.delete()  
        except VeDatSan.DoesNotExist:
            return HttpResponse("Vé không tồn tại!", status=400)
    return render(request, "home/r2checkin.html", {'lve': lve})

def Confirm(request):
    danh_sach=VeDatSan.objects.all()
    return render(request,'home/r3confirm.html',{'danh_sach':danh_sach})

def Vip(request):
    danh_sach_vip=Voucher_model.objects.all()
    return render(request,"home/r3vip.html",{'danh_sach_vip':danh_sach_vip})

def Voucher(request):
    if request.method == 'POST':
        form = Gangzbit(request.POST)
        if form.is_valid():
            form.save()
            return redirect('r3vip')  # Chuyển hướng sau khi lưu thành công
    else:
        form = Gangzbit()

    return render(request, 'home/r3voucher.html', {'form': form})

def delete_voucher(request,voucher):
    v=get_object_or_404(Voucher_model,voucher=voucher)
    v.delete()
    return render(request, 'home/r3vip.html')