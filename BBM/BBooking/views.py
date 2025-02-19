from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Court, VeDatSan, San, TimeSlot, Flag
from .forms import VeDatSanForm, FlagForm
from django.contrib import messages
from django.urls import reverse

@login_required(login_url='login')
def booking(request, maCourt):
    court = get_object_or_404(Court, maCourt=maCourt)
    available_san = San.objects.filter(court=court)

    # Lấy sân được chọn từ request (nếu có)
    selected_san_id = request.GET.get('san')  # Lấy từ URL query param
    if selected_san_id:
        selected_san = get_object_or_404(San, maSan=selected_san_id, court=court)
        available_timeslots = TimeSlot.objects.filter(san=selected_san, flag=True)
    else:
        available_timeslots = TimeSlot.objects.none()  # Không hiển thị timeslot nếu chưa chọn sân

    return render(request, "home/booking.html", {
        'court': court,
        'available_san': available_san,
        'available_timeslots': available_timeslots,
        'selected_san_id': selected_san_id
    })

def dateBooking(request, maCourt):
    court = get_object_or_404(Court, maCourt=maCourt)
    timeslots = TimeSlot.objects.filter(court=court)
    sans=San.objects.filter(court=court)
    if request.method == "POST":
        form = FlagForm(request.POST)
        if form.is_valid():
            # form.save()
            ts = form.cleaned_data.get("timeslot")
            d = form.cleaned_data.get("date")
            s = form.cleaned_data.get("san")
            # flag=Flag.objects.filter(san=s,timeslot=ts,date=d).first()
            url = reverse("voucher", kwargs={"maCourt": maCourt, "ts":ts, "d":d, "s":s})
            return redirect(url)
        else:
            messages.error(request, "Thời gian này sân đã được đặt trước đó!")
    else:
        form = FlagForm()
    return render(request, 'home/dateBooking.html', {"form": form, "timeslots": timeslots, 'court':court, 'sans':sans})

def voucher(request, maCourt, ts, d, s):
    return render(request, "home/InputDiscount.html", {"maCourt":maCourt, "ts":ts, "d":d, "s":s})

def tongTien(request, maCourt, flagid):
    return render(request, "home/Tongtien.html", {"maCourt":maCourt, "flagid":flagid})