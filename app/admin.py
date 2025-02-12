from django.contrib import admin # type: ignore
from .models import Customer,System_Admin,Manager,Staff
# Register your models here.
admin.site.register(Customer)
admin.site.register(System_Admin)
admin.site.register(Manager)
admin.site.register(Staff)

