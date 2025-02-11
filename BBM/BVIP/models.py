from django.db import models

# Create your models here.
class VIP(models.Model):
    maVip = models.CharField(default='',max_length=10, primary_key=True)
    diem = models.IntegerField(default=0)
    lvVIP = models.IntegerField(default=0)
    phanTramGiamGia=models.FloatField(default=0)
    def __str__(self):
        return f"{self.maVip}"