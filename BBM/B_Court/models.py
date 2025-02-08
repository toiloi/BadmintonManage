from django.db import models

# Create your models here.
class San(models.Model):
    maSan = models.CharField(default='',max_length=255)
    tinhTrang = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.maSan} {self.tinhTrang}"

class Court(models.Model):
    san=models.ForeignKey(San, on_delete=models.CASCADE)
    maCourt = models.CharField(default='',max_length=255)
    name = models.CharField(default='',max_length=255)
    address = models.CharField(default='',max_length=255)
    descreption = models.CharField(default='',max_length=255)
    def __str__(self):
        return f"{self.maCourt} {self.name} {self.address}"