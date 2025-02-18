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



class DailyStat(models.Model):
    date = models.DateField()
    revenue = models.DecimalField(max_digits=10, decimal_places=2)
    bookings = models.IntegerField()

class Transaction(models.Model):
    STATUS_CHOICES = [
        ('Đã Thanh Toán', 'Đã Thanh Toán'),
        ('Chưa Thanh Toán', 'Chưa Thanh Toán'),
    ]

    transaction_id = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    date = models.DateTimeField()  # Sử dụng DateTimeField để lưu cả ngày và giờ
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Chưa Thanh Toán')
    # Thêm các trường khác nếu cần

