from django.contrib import admin
from .models import Court, San, Sonha, Duong, Phuong, Quan, Tinh, CourtStaff, DailyStat, Transaction

# Register your models here.

class CourtAd(admin.ModelAdmin):
  list_display = ("maCourt", "name",)

class SanAd(admin.ModelAdmin):
  list_display = ("maSan", "tinhTrang",)

class SonhaAd(admin.ModelAdmin):
  list_display = ("name",)
  
class DuongAd(admin.ModelAdmin):
  list_display = ("name",)

class PhuongAd(admin.ModelAdmin):
  list_display = ("name",)

class QuanAd(admin.ModelAdmin):
  list_display = ("name",)

class TinhAd(admin.ModelAdmin):
  list_display = ("name",)

class CourtStaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'role')
    search_fields = ('name', 'email', 'phone', 'role')

class DailyStatAdmin(admin.ModelAdmin):
    list_display = ('date', 'revenue', 'bookings')
    search_fields = ('date',)


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'customer_name', 'date', 'amount', 'status')
    search_fields = ('transaction_id', 'customer_name', 'date', 'status')

admin.site.register(Court, CourtAd)
admin.site.register(San, SanAd)
admin.site.register(Sonha, SonhaAd)
admin.site.register(Duong, DuongAd)
admin.site.register(Phuong, PhuongAd)
admin.site.register(Quan, QuanAd)
admin.site.register(Tinh, TinhAd)
admin.site.register(CourtStaff, CourtStaffAdmin)
admin.site.register(DailyStat, DailyStatAdmin)
admin.site.register(Transaction, TransactionAdmin)
