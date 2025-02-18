from django.db import models
from BUser.models import User
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your models here.
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'role', 'gender', 'sdt']


class Transaction(models.Model):
    transaction_id = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    # Thêm các trường khác nếu cần

class staffRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()


class Transaction(models.Model):
    transaction_id = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    # Thêm các trường khác nếu cần

class DailyStat(models.Model):
    date = models.DateField()
    revenue = models.DecimalField(max_digits=10, decimal_places=2)
    bookings = models.IntegerField()

class CourtStaff(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=50)