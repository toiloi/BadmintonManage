from django.contrib import admin
from .models import VIP

# Register your models here.
# admin.site.register(VIP)

class VIPAdmin(admin.ModelAdmin):
  list_display = ("maVip",)
  
admin.site.register(VIP, VIPAdmin)