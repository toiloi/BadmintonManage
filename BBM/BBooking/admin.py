from django.contrib import admin
from .models import TimeSlot, VeDatSan, CheckIn

# Register your models here.
# admin.site.register(TimeSlot)
# admin.site.register(VeDatSan)
# admin.site.register(HoaDon)

class TimeSlotAdmin(admin.ModelAdmin):
  list_display = ("timeslot", "san")

class VeDatSanAdmin(admin.ModelAdmin):
  list_display = ("date", "timeslot", "checkin")

class CheckInAdmin(admin.ModelAdmin):
  list_display = ("vedatsan", "courtstaff",)
  
admin.site.register(TimeSlot, TimeSlotAdmin)
admin.site.register(VeDatSan, VeDatSanAdmin)
admin.site.register(CheckIn, CheckInAdmin)