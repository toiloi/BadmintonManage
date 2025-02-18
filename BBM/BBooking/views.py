from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Court, VeDatSan, San, TimeSlot
from .forms import VeDatSanForm

@login_required(login_url='login')
def datSan(request, maCourt):
    court = get_object_or_404(Court, maCourt=maCourt)
    available_san = San.objects.filter(court=court)

    # Lấy sân được chọn từ request (nếu có)
    selected_san_id = request.GET.get('san')  # Lấy từ URL query param
    if selected_san_id:
        selected_san = get_object_or_404(San, maSan=selected_san_id, court=court)
        available_timeslots = TimeSlot.objects.filter(san=selected_san, flag=True)
    else:
        available_timeslots = TimeSlot.objects.none()  # Không hiển thị timeslot nếu chưa chọn sân

    return render(request, "home/datsan.html", {
        'court': court,
        'available_san': available_san,
        'available_timeslots': available_timeslots,
        'selected_san_id': selected_san_id
    })