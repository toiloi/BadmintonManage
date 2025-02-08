from django.contrib import admin
from .models import Court, San

# Register your models here.
# admin.site.register(Court)
# admin.site.register(San)

class CourtAd(admin.ModelAdmin):
  list_display = ("maCourt", "name", "address",)

class SanAd(admin.ModelAdmin):
  list_display = ("maSan", "tinhTrang",)
  
admin.site.register(Court, CourtAd)
admin.site.register(San, SanAd)
