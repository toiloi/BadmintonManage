from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Court, VeDatSan, San, TimeSlot, Flag, Voucher
from .forms import VeDatSanForm, FlagForm
from django.contrib import messages
from django.urls import reverse
from datetime import datetime,timedelta

@login_required(login_url='login')
def booking(request, maCourt):
    if request.method == "POST":
        tp=request.POST.get("type")
        if tp=="codinh":
            url=reverse('fixedBooking', kwargs={'maCourt':maCourt, 'tp':tp})
            return redirect(url)
        elif tp=="theongay":
            url=reverse('dateBooking' , kwargs={'maCourt':maCourt, 'tp':tp})
            return redirect(url)
        else:
            url=reverse('flexBookinf')
            return redirect(url)
    return render(request, "home/booking.html")

def fixedBooking(request, maCourt, tp):
    court = get_object_or_404(Court, maCourt=maCourt)
    timeslots = TimeSlot.objects.filter(court=court)
    sans=San.objects.filter(court=court)
    if request.method == "POST":
        form = FlagForm(request.POST)
        if form.is_valid():
            # form.save()
            ts = form.cleaned_data.get("timeslot")
            d = form.cleaned_data.get("date")
            san = form.cleaned_data.get("san")
            s=san.maSan
            # flag=Flag.objects.filter(san=s,timeslot=ts,date=d).first()
            url = reverse("voucher", kwargs={"maCourt": maCourt, "tp":tp, "ts":ts, "d":d, "s":s})
            return redirect(url)
        else:
            messages.error(request, "Thời gian này sân đã được đặt trước đó!")
    else:
        form = FlagForm()
    return render(request, "home/FixedBooking.html", {"form": form, "timeslots": timeslots, 'court':court, 'sans':sans})

def flexBooking(request, maCourt):
    return render(request, "home/FlexBooking.html")

def dateBooking(request, maCourt, tp):
    court = get_object_or_404(Court, maCourt=maCourt)
    timeslots = TimeSlot.objects.filter(court=court)
    sans=San.objects.filter(court=court)
    if request.method == "POST":
        form = FlagForm(request.POST)
        if form.is_valid():
            # form.save()
            ts = form.cleaned_data.get("timeslot")
            d = form.cleaned_data.get("date")
            san = form.cleaned_data.get("san")
            s=san.maSan
            # flag=Flag.objects.filter(san=s,timeslot=ts,date=d).first()
            url = reverse("voucher", kwargs={"maCourt": maCourt, "tp":tp, "ts":ts, "d":d, "s":s})
            return redirect(url)
        else:
            messages.error(request, "Thời gian này sân đã được đặt trước đó!")
    else:
        form = FlagForm()
    return render(request, 'home/dateBooking.html', {"form": form, "timeslots": timeslots, 'court':court, 'sans':sans})

def voucher(request, maCourt, tp, ts, d, s):
    court = get_object_or_404(Court, maCourt=maCourt)
    if request.method == "POST":
            voucher_id = request.POST.get("voucher", None)
            v = Voucher.objects.filter(voucher=voucher_id, court=court).first() if voucher_id else None
            san=get_object_or_404(San, maSan=s)
            gia_san = san.court.price
            if tp=="theongay":
                tien = gia_san
            elif tp=="codinh":
                tien =gia_san*4
            else:
                tien=gia_san
            if v:
                tien -= (tien * v.percent / 100)
            tien=int(tien)
            url = reverse("tongtien", kwargs={"maCourt": maCourt, "tp":tp, "ts":ts, "d":d, "s":s, "tien":tien})
            return redirect(url)
    return render(request, "home/InputDiscount.html", {"maCourt":maCourt, "tp":tp, "ts":ts, "d":d, "s":s})

def TongTien(request, maCourt, tp, ts, d, s, tien):
    if request.method == "POST":
        court=get_object_or_404(Court,maCourt=maCourt)
        san=get_object_or_404(San, maSan=s)
        ts = datetime.strptime(ts, "%H:%M:%S").time()
        ts=get_object_or_404(TimeSlot, court=court, timeslot=ts)
        d = datetime.strptime(d, "%Y-%m-%d").date()
        flag=Flag.objects.create(
            san=san,
            timeslot=ts,
            date=d
        )
        ve=VeDatSan.objects.create(
            flag=flag,
            customer=request.user,
            tongTien=tien,
        )
        if tp == "codinh":
            for i in range(3):
                d += timedelta(days=7)
                flag=Flag.objects.create(
                    san=san,
                    timeslot=ts,
                    date=d
                )
        url = reverse("successBooking", kwargs={"maCourt": maCourt})
        return redirect(url)
    return render(request, "home/Tongtien.html", {"maCourt":maCourt, "tp":tp, "ts":ts, "d":d, "s":s, "tien":tien})

def successBooking(request, maCourt):
    return render(request, "home/booking-success.html", {"maCourt":maCourt})