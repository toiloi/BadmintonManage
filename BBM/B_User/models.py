from django.db import models
from B_Court.models import Court

# Create your models here.
class Account(models.Model):
    roleId = models.IntegerField(default='0')
    useName= models.CharField(default='', max_length=20)
    password = models.CharField(default='',max_length=20)

class User(models.Model):
    sdt= models.IntegerField(default=0)
    gmail = models.CharField(default='',max_length=255)
    address = models.CharField(default='',max_length=255)
    fullName = models.CharField(default='',max_length=255)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Position(models.Model):
    soNha = models.CharField(max_length=255,default='')
    huyen = models.CharField(max_length=255,default='')
    tinh = models.CharField(max_length=255,default='')
    quocGia = models.CharField(max_length=255,default='')

class Customer(User):
    note = models.CharField(max_length=255,default='')
    position = models.ForeignKey(Position,on_delete=models.CASCADE)

class CourtStaff(User):
    court = models.ForeignKey(Court, on_delete=models.CASCADE)

class CourtManager(User):
    court = models.ForeignKey(Court, on_delete=models.CASCADE)