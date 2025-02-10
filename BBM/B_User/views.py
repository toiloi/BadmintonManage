from django.shortcuts import render
from django.http import HttpResponse

def Position(request):
    return HttpResponse("Hello world!")

def CourtStaff(request):
    return HttpResponse("Hello world!")

def CourtManager(request):
    return HttpResponse("Hello world!")

def Customer(request):
    return HttpResponse("Hello world!")