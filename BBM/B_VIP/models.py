from django.db import models

# Create your models here.
class VIP(models.Model):
    maVip = models.CharField(default='',max_length=255)
    diem = models.IntegerField(default=0)
    lvVIP = models.IntegerField(default=0)
    phanTramGiamGia=models.FloatField(default=0)