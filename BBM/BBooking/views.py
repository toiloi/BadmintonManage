from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Court, VeDatSan, San, TimeSlot, Flag, Voucher, flexTime
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
        elif tp=="theongay":
            url=reverse('dateBooking' , kwargs={'maCourt':maCourt, 'tp':tp})
        else:
            url=reverse('flexBooking' ,kwargs={'maCourt':maCourt, 'tp':tp})
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

def flexBooking(request, maCourt, tp):
    court = get_object_or_404(Court, maCourt=maCourt)
    return render(request, "home/FlexibleBooking.html", {'court':court, 'tp':tp})

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
            type=tp,
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
                ve=VeDatSan.objects.create(
                type=tp,
                flag=flag,
                customer=request.user,
                tongTien=tien,
        )
        url = reverse("successBooking", kwargs={"maCourt": maCourt})
        return redirect(url)
    return render(request, "home/Tongtien.html", {"maCourt":maCourt, "tp":tp, "ts":ts, "d":d, "s":s, "tien":tien})

def successBooking(request, maCourt):
    return render(request, "home/booking-success.html", {"maCourt":maCourt})

def themGio(request, maCourt, tp):
    if request.method == "POST":
        time = request.POST.get("time")
        url = reverse("voucher1", kwargs={"maCourt": maCourt, "tp":tp, "time":time})
        return redirect(url)
    return render(request, "home/HourType.html", {"maCourt":maCourt, "tp":tp})

def voucher1(request, maCourt, tp, time):
    court = get_object_or_404(Court, maCourt=maCourt)
    if request.method == "POST":
            voucher_id = request.POST.get("voucher", None)
            v = Voucher.objects.filter(voucher=voucher_id, court=court).first() if voucher_id else None
            gia_san = court.price
            tien=gia_san*time
            if v:
                tien -= (tien * v.percent / 100)
            tien=int(tien)
            url = reverse("tongtien1", kwargs={"maCourt": maCourt, "tp":tp, "time":time, "tien":tien})
            return redirect(url)
    return render(request, "home/InputDiscount.html", {"maCourt":maCourt, "tp":tp, "time":time})

def TongTien1(request, maCourt, tp, time, tien):
    if request.method == "POST":
        court=get_object_or_404(Court,maCourt=maCourt)
        user=request.user
        check=flexTime.objects.filter(court=court, customer=user).exists()
        if check:
            ft=get_object_or_404(flexTime, court=court, customer=user)
            ft.time+=time
            ft.save()
        else:
            ft=flexTime.objects.create(
                court=court,
                customer=user,
                time=time
            )
        url = reverse("successBooking", kwargs={"maCourt": maCourt})
        return redirect(url)
    return render(request, "home/Tongtien1.html", {"maCourt":maCourt, "tp":tp, "time":time, "tien":tien})

def themLich(request, maCourt, tp):
    user=request.user
    court = get_object_or_404(Court, maCourt=maCourt)
    time=get_object_or_404(flexTime,court=court,customer=user)
    timeslots = TimeSlot.objects.filter(court=court)
    sans=San.objects.filter(court=court)
    if request.method == "POST":
        form = FlagForm(request.POST)
        if form.is_valid():
            form.save()
            ts = form.cleaned_data.get("timeslot")
            d = form.cleaned_data.get("date")
            san = form.cleaned_data.get("san")
            flag=get_object_or_404(Flag, timeslot=ts, date=d, san=san)
            ve=VeDatSan.objects.create(
            type=tp,
            flag=flag,
            customer=request.user
            )
            url = reverse("successBooking", kwargs={"maCourt": maCourt})
            time.time-=1
            time.save()
            return redirect(url)
        else:
            messages.error(request, "Thời gian này sân đã được đặt trước đó!")
    else:
        form = FlagForm()
    return render(request, "home/CalendarType.html", {"maCourt":maCourt, "form": form, "tp":tp, "timeslots": timeslots, 'court':court, 'sans':sans, 'time':time})