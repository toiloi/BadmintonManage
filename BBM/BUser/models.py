from django.db import models
from BCourt.models import Court
from django.contrib.auth.models import AbstractUser

# Create your models here.

# class Account(models.Model):
#     roleId = models.IntegerField(default='1')
#     useName= models.CharField(default='', max_length=20, primary_key=True)
#     password = models.CharField(default='',max_length=20)
#     def __str__(self):
#         return f"{self.useName} {self.roleId}"

class User(AbstractUser):
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('courtstaff', 'Court Staff'),
        ('courtmanager', 'Court Manager'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    sdt= models.IntegerField(default=0, null=True, blank=True)
    def __str__(self):
        return f"{self.first_name} {self.username}"


class CourtStaff(User):
    court1 = models.ForeignKey(Court, on_delete=models.CASCADE,  null=True, blank=True)
    def __str__(self):
        return f"{self.first_name} {self.username} {self.court1}"