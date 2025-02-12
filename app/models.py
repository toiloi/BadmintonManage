from django.db import models # type: ignore
from django.contrib.auth.hashers import make_password,check_password

# Create your models here.
class Customer(models.Model):
    account_name=models.CharField(max_length=255)
    pw =models.CharField(max_length=255)
    def save_pw(self,*args,**kwargs):
        if not self.pw.startswith("pbkdf2_"):
            self.pw=make_password(self.pw)
        super.save(*args,**kwargs)
    def __str__(self):
        return f"{self.account_name} {self.pw}"
    
class System_Admin(models.Model):
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    def __str__(self):
        return f"{self.username} {self.password}"
    
class Manager(models.Model):
    fullName=models.CharField(max_length=255)
    account=models.CharField(max_length=255)
    def __str__(self):
        return f"{self.fullName} {self.account}"
    
class Staff(models.Model):
    def __str__(self):
        return super().__str__(self)
        
class Court(models.Model):
    def __str__(self):
        return super().__str__(self)
    
class ListAccount(models.Model):
    def __str__(self):
        return super().__str__(self)
