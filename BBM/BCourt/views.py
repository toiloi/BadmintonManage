from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Court
from BUser.models import User
from django.contrib.auth.forms import UserCreationForm
from home.models import RegisterForm
from BBooking.models import VeDatSan

def home(request):
    return render(request, 'home/home.html')

def role_required(*roles):
    def check_role(user):
        return user.is_authenticated and user.role in roles
    return user_passes_test(check_role, login_url="login")

def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
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
            role = getattr(user, "role", None)

            print(f"User {username} logged in with role: {role}")  # Debug

            if role in ["customer", "courtstaff", "courtmanager"]:
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
# @role_required("customer", "courtstaff", "courtmanager")
def role(request):
    user = request.user
    role = getattr(user, "role", None)

    print(f"User {user.username} has role: {role}")  # Debug

    if role == "customer":
        lc = Court.objects.all()
        return render(request, "home/role1.html", {"lc": lc})
    elif role == "courtstaff":
        return render(request, "home/role2.html")
    elif role == "courtmanager":
        lc = Court.objects.all()
        return render(request, "home/role3.html", {"lc": lc})
    else:
        return HttpResponse("Không xác định được vai trò của bạn.", status=400)

def history(request):
    user = request.user
    lb = VeDatSan.objects.filter(customer=user)
    return render(request, 'home/history.html', {"lb": lb})

def deleteHistory(request, ve):
    return render(request, 'home/deleteHistory.html', {"ve": ve})

def chiTiet(request, maCourt):
    court = get_object_or_404(Court, maCourt=maCourt)
    return render(request, "home/detail.html", {"court": court})

def search(request):
    query = request.GET.get('q')
    results = Court.objects.filter(name__icontains=query) if query else []
    return render(request, "home/search.html", {'results': results, 'query': query})

def staffList(request):
    lc = User.objects.filter(role="courtstaff")
    return render(request, "home/staffList.html", {"lc": lc})

def xetduyetNhanVien(request):
    return render(request, "home/xetduyetNhanVien.html")

def chamCong(request):
    return render(request, "home/chamcong.html")

def payment(request):
    return render(request, "home/payment.html")

def Revenue(request):
    return render(request, "home/revenue.html")

def courtFilter(request):
    selected_price = request.GET.get("price", "")
    selected_tinh = request.GET.get("tinh", "")
    selected_quan = request.GET.get("quan", "")
    selected_phuong = request.GET.get("phuong", "")
    selected_duong = request.GET.get("duong", "")

    courts = Court.objects.all()

    if selected_price == "low":
        courts = courts.filter(price__lt=50000)
    elif selected_price == "medium":
        courts = courts.filter(price__gte=50000, price__lte=100000)
    elif selected_price == "high":
        courts = courts.filter(price__gt=100000)

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


def chamCong(request):
    # Só tiền lương trên 1 ngày
    daily_wage = input("Nhập số tiền lương trên 1 ngày: ")

    # Lấy danh sách nhân viên và tính toán số ngày công và lương
    staff_list = User.objects.filter(role="courtstaff").annotate(
        days_worked=F('days_worked'),  # Số ngày công
        total_salary=F('days_worked') * daily_wage
    )

    context = {
        'staff_list': staff_list,
    }
    return render(request, "home/chamCong.html", context)




#Xet duyet nhan vien
def approveStaff(request, staff_id):
    staff = get_object_or_404(User, id=staff_id, role="courtstaff")
    staff.is_active = True  # Hoặc bất kỳ logic nào để duyệt nhân viên
    staff.save()
    staff_json = serializers.serialize('json', [staff])
    return JsonResponse({"status": "approved", "staff": staff_json})

#Từ chối nhân viên``
def rejectStaff(request, staff_id):
    staff = get_object_or_404(User, id=staff_id, role="courtstaff")
    staff.delete()  # Hoặc bất kỳ logic nào để từ chối nhân viên
    return JsonResponse({"status": "rejected"})


def Revenue(request):
    # Lấy ngày đầu tiên và ngày cuối cùng của tháng hiện tại
    today = datetime.today()
    first_day_of_month = today.replace(day=1)
    last_day_of_month = (first_day_of_month + timedelta(days=32)).replace(day=1) - timedelta(days=1)

    # Tính tổng doanh thu và số lượt đặt sân trong tháng hiện tại
    total_revenue = VeDatSan.objects.filter(flag__date__range=[first_day_of_month, last_day_of_month]).aggregate(Sum('tongTien'))['tongTien__sum'] or 0
    total_bookings = VeDatSan.objects.filter(flag__date__range=[first_day_of_month, last_day_of_month]).count()

    # Tính doanh thu và số lượt đặt sân hàng ngày trong tháng hiện tại
    daily_stats = VeDatSan.objects.filter(flag__date__range=[first_day_of_month, last_day_of_month]).values('flag__date').annotate(revenue=Sum('tongTien'), bookings=Count('maVe')).order_by('flag__date')

    context = {
        'total_revenue': total_revenue,
        'total_bookings': total_bookings,
        'daily_stats': daily_stats,
    }

    return render(request, "home/Revenue.html", context)


def payment(request):
    transactions = VeDatSan.objects.all()
    context = {
        'transactions': transactions,
    }
    return render(request, "home/payment.html", context)


