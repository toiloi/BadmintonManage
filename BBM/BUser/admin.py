from django.contrib import admin
from .models import User, CourtStaff

class UserAdmin(admin.ModelAdmin):
  list_display = ("username", "first_name", )
  
admin.site.register(User, UserAdmin)

class CourtStaffAdmin(admin.ModelAdmin):
  list_display = ("username", "first_name",)
  
admin.site.register(CourtStaff, CourtStaffAdmin)