from django.shortcuts import render
from django.http import HttpResponse
from .models import VeDatSan as VeDatSan_model


def TimeSlot(request):
    return HttpResponse("Hello world!")

def VeDatSan1(request):
    danh_sach=VeDatSan_model.objects.all()
    return render(request,'home/confirm.html',{'danh_sach':danh_sach})

def HoaDon(request):
    return HttpResponse("Hello world!")