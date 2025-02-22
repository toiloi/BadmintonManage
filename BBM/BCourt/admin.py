from django.contrib import admin
from .models import Court, San, Address, Rating, xinViec,CourtTimeSlot

# Register your models here.

class CourtAd(admin.ModelAdmin):
  list_display = ("maCourt", "name",)

class SanAd(admin.ModelAdmin):
  list_display = ("maSan", "numSan",)

class AddressAd(admin.ModelAdmin):
  list_display = ("soNha", "duong", "phuong", "quan", "tinh")

class RatingAd(admin.ModelAdmin):
  list_display = ("customer", "rate",)

class CourtTimeSlotAd(admin.ModelAdmin):
  list_display=("court","date","time")

class xinViecAd(admin.ModelAdmin):
  list_display = ("court", "courtStaff",)

admin.site.register(Court, CourtAd)
admin.site.register(San, SanAd)
admin.site.register(Address, AddressAd)
admin.site.register(Rating, RatingAd)
admin.site.register(xinViec, xinViecAd)
admin.site.register(CourtTimeSlot,CourtTimeSlotAd)