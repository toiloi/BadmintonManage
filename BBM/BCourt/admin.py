from django.contrib import admin
from .models import Court, San, Address

# Register your models here.
# admin.site.register(Court)
# admin.site.register(San)

class CourtAd(admin.ModelAdmin):
  list_display = ("maCourt", "name", "address",)

class SanAd(admin.ModelAdmin):
  list_display = ("maSan", "tinhTrang",)

class AddressAd(admin.ModelAdmin):
  list_display = ("soNha", "xa", "huyen", "tinh", "quocGia")
  
admin.site.register(Court, CourtAd)
admin.site.register(San, SanAd)
admin.site.register(Address, AddressAd)
