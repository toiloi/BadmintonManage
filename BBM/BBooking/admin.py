from django.contrib import admin
from .models import TimeSlot, VeDatSan, CheckIn, Flag, Voucher, flexTime

class TimeSlotAdmin(admin.ModelAdmin):
  list_display = ("timeslot", "court")

class VeDatSanAdmin(admin.ModelAdmin):
  list_display = ("maVe", "checkin")

class CheckInAdmin(admin.ModelAdmin):
  list_display = ("vedatsan", "courtstaff",)

class FlagAdmin(admin.ModelAdmin):
  list_display = ("timeslot", "date", "san")

class VoucherAdmin(admin.ModelAdmin):
  list_display = ("voucher", "court", "percent")

class flexTimeAdmin(admin.ModelAdmin):
  list_display = ("customer", "court", "time")
  
admin.site.register(TimeSlot, TimeSlotAdmin)
admin.site.register(VeDatSan, VeDatSanAdmin)
admin.site.register(CheckIn, CheckInAdmin)
admin.site.register(Flag, FlagAdmin)
admin.site.register(Voucher, VoucherAdmin)
admin.site.register(flexTime, flexTimeAdmin)