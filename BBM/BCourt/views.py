from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Court, Address, San
from .forms import CourtForm, AddressForm, SanForm
from django.urls import reverse
from BBooking.models import TimeSlot



@login_required(login_url="login")
def add_court(request):
    if request.method == 'POST':
        court_form = CourtForm(request.POST, request.FILES)
        address_form = AddressForm(request.POST)

        if court_form.is_valid() and address_form.is_valid():
            address, created = Address.objects.get_or_create(
                soNha=address_form.cleaned_data['soNha'],
                duong=address_form.cleaned_data['duong'],
                phuong=address_form.cleaned_data['phuong'],
                quan=address_form.cleaned_data['quan'],
                tinh=address_form.cleaned_data['tinh']
            )

            court = court_form.save(commit=False)
            court.address = address
            court.courtManager = request.user  # ✅ Gán courtManager là user đang đăng nhập
            court.save()

            messages.success(request, "Thêm sân thành công!")
            return redirect('r3manage_court')

        else:
            print("Lỗi form:", court_form.errors, address_form.errors)

    else:
        court_form = CourtForm()
        address_form = AddressForm()

    return render(request, "home/r3add_court.html", {
        'court_form': court_form,
        'address_form': address_form
    })

@login_required(login_url="login")
def manage_court(request):
    courts = Court.objects.all()
    print("Danh sách sân:", courts)  # Kiểm tra dữ liệu trong terminal
    return render(request, "home/r3manage_court.html", {"courts": courts})




@login_required(login_url="login")
def chiTiet(request, maCourt):
    """Xem chi tiết sân"""
    court = get_object_or_404(Court, maCourt=maCourt)
    sans = San.objects.filter(court=court)
    times=TimeSlot.objects.filter(court=court)
    print(times)
    return render(request, "home/r3detail.html", {"court": court, "sans": sans,"times":times})


@login_required(login_url="login")
def add_san(request, maCourt):
    court = get_object_or_404(Court, maCourt=maCourt)

    if request.method == 'POST':
        san_form = SanForm(request.POST)
        if san_form.is_valid():
            san = san_form.save(commit=False)
            san.court = court
            san.save()
            messages.success(request, "Thêm sân thành công!")
            url = reverse("chiTiet", kwargs={"maCourt": maCourt})
            return redirect(url)
        else:
            print("Lỗi form:", san_form.errors)
    else:
        san_form = SanForm()

    return render(request, 'home/r3add_san.html', {
        'san_form': san_form,
        'court': court,
    })


@login_required(login_url="login")
def delete_court(request, maCourt):
    court = get_object_or_404(Court, maCourt=maCourt)

    if request.method == "POST":
        court.delete()
        messages.success(request, f"Đã xóa sân {court.name} thành công!")
        return redirect("r3manage_court")  # Điều hướng về trang quản lý sân

    return render(request, "home/r3manage_court.html", {"court": court})


@login_required(login_url="login")
def delete_san(request, maSan):
    san = get_object_or_404(San, maSan=maSan)
    maCourt = san.court.maCourt  # Lấy mã sân cha để quay lại trang chi tiết

    if request.method == "POST":
        maCourt = san.court.maCourt  # Lấy mã sân cha để quay lại trang chi tiết
        san.delete()
        messages.success(request, f"Đã xóa sân {san.numSan} thành công!")
        return redirect("chiTiet", maCourt=maCourt)  # Điều hướng về trang chi tiết sân

    return redirect("r3manage_court")

