from django.contrib import admin
from .models import Court, San, Address, Rating

# Register your models here.

class CourtAd(admin.ModelAdmin):
  list_display = ("maCourt", "name",)

class SanAd(admin.ModelAdmin):
  list_display = ("maSan", "numSan",)

class AddressAd(admin.ModelAdmin):
  list_display = ("soNha", "duong", "phuong", "quan", "tinh")

class RatingAd(admin.ModelAdmin):
  list_display = ("customer", "rate",)

admin.site.register(Court, CourtAd)
admin.site.register(San, SanAd)
admin.site.register(Address, AddressAd)
admin.site.register(Rating, RatingAd)