from django.contrib import admin
from .models import Court, San, Sonha, Duong, Phuong, Quan, Tinh, Rating

# Register your models here.

class CourtAd(admin.ModelAdmin):
  list_display = ("maCourt", "name",)

class SanAd(admin.ModelAdmin):
  list_display = ("maSan", "numSan",)

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

class RatingAd(admin.ModelAdmin):
  list_display = ("customer", "rate",)

admin.site.register(Court, CourtAd)
admin.site.register(San, SanAd)
admin.site.register(Sonha, SonhaAd)
admin.site.register(Duong, DuongAd)
admin.site.register(Phuong, PhuongAd)
admin.site.register(Quan, QuanAd)
admin.site.register(Tinh, TinhAd)
admin.site.register(Rating, RatingAd)