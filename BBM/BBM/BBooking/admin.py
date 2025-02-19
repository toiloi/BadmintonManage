from django.contrib import admin
from .models import TimeSlot, VeDatSan, HoaDon, Voucher

# Register your models here.
# admin.site.register(TimeSlot)
# admin.site.register(VeDatSan)
# admin.site.register(HoaDon)

class TimeSlotAdmin(admin.ModelAdmin):
  list_display = ("timeslot",)

class VeDatSanAdmin(admin.ModelAdmin):
  list_display = ("san", "date", "timeslot",)

class HoaDonAdmin(admin.ModelAdmin):
  list_display = ("maHoaDon", "ngayTao",)
  
class VoucherAdmin(admin.ModelAdmin):
  list_display=("voucher","court","percent")
  
admin.site.register(TimeSlot, TimeSlotAdmin)
admin.site.register(VeDatSan, VeDatSanAdmin)
admin.site.register(HoaDon, HoaDonAdmin)
admin.site.register(Voucher,VoucherAdmin)