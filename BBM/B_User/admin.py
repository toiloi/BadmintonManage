from django.contrib import admin
from .models import Position, CourtStaff, CourtManager, Customer

# Register your models here.
# admin.site.register(Account)
# admin.site.register(Position)
# admin.site.register(CourtManager)
# admin.site.register(CourtStaff)
# admin.site.register(Customer)

class PositionAdmin(admin.ModelAdmin):
  list_display = ("soNha", "xa", "huyen", "tinh", "quocGia")

class CourtManagerAdmin(admin.ModelAdmin):
  list_display = ("fullName", "account",)

class CourtStaffAdmin(admin.ModelAdmin):
  list_display = ("fullName", "account", "court")

class CustomerAdmin(admin.ModelAdmin):
  list_display = ("fullName", "account",)

admin.site.register(Position, PositionAdmin)

admin.site.register(CourtManager, CourtManagerAdmin)

admin.site.register(CourtStaff, CourtStaffAdmin)

admin.site.register(Customer, CustomerAdmin)
  

