from django.contrib import admin
from .models import TimeSlot, VeDatSan, HoaDon

# Register your models here.
# admin.site.register(TimeSlot)
# admin.site.register(VeDatSan)
# admin.site.register(HoaDon)

class TimeSlotAdmin(admin.ModelAdmin):
  list_display = ("timeslot", "court",)

class VeDatSanAdmin(admin.ModelAdmin):
  list_display = ("maVe", "timeslot",)

class HoaDonAdmin(admin.ModelAdmin):
  list_display = ("maHoaDon", "ngayTao",)
  
admin.site.register(TimeSlot, TimeSlotAdmin)
admin.site.register(VeDatSan, VeDatSanAdmin)
admin.site.register(HoaDon, HoaDonAdmin)