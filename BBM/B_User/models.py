from django.db import models
from B_Court.models import Court
from django.contrib.auth.models import User

# Create your models here.

# class Account(models.Model):
#     roleId = models.IntegerField(default='1')
#     useName= models.CharField(default='', max_length=20, primary_key=True)
#     password = models.CharField(default='',max_length=20)
#     def __str__(self):
#         return f"{self.useName} {self.roleId}"

class Userr(models.Model):
    roleId = models.IntegerField(default='1')
    fullName = models.CharField(default='',max_length=255)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    sdt= models.IntegerField(default=0, null=True, blank=True)
    gmail = models.CharField(default='',max_length=255)
    account = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    class Meta:
        abstract = True

class Position(models.Model):
    soNha = models.CharField(max_length=255,default='')
    xa = models.CharField(max_length=255,default='')
    huyen = models.CharField(max_length=255,default='')
    tinh = models.CharField(max_length=255,default='')
    quocGia = models.CharField(max_length=255,default='')
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["soNha", "xa", "huyen", "tinh", "quocGia"], name="unique_position")
        ]
    def __str__(self):
        return f"{self.soNha} {self.huyen} {self.tinh} {self.quocGia}"

class Customer(Userr):
    position = models.ForeignKey(Position,on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f"{self.fullName} {self.account}"
    
class CourtManager(Userr):
    def __str__(self):
        return f"{self.fullName} {self.account}"

class CourtStaff(Userr):
    court = models.ForeignKey(Court, on_delete=models.CASCADE,  null=True, blank=True)
    def __str__(self):
        return f"{self.fullName} {self.account} {self.court}"