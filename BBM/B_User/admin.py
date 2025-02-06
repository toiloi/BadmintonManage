from django.contrib import admin
from .models import Account, Position, CourtStaff, CourtManager, Customer

# Register your models here.
admin.site.register(Account)
admin.site.register(Position)
admin.site.register(CourtManager)
admin.site.register(CourtStaff)
admin.site.register(Customer)
