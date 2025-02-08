from django.db import models
from B_Court.models import Court, San
from B_User.models import Customer, CourtStaff

# Create your models here.
class TimeSlot(models.Model):
    timeslot = models.DateTimeField()
    court = models.ForeignKey(Court,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.timeslot} {self.court}"

class VeDatSan(models.Model):
    maVe = models.CharField(default='',max_length=255)
    thanhToan = models.BooleanField(default=True)
    san = models.ForeignKey(San, on_delete=models.CASCADE)
    timeslot = models.ForeignKey(TimeSlot,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.maVe} {self.timeslot}"

class HoaDon(models.Model):
    maHoaDon = models.CharField(default='',max_length=255)
    tongTien = models.IntegerField(default=0)
    ngayTao = models.DateTimeField()
    note = models.CharField(default='',max_length=255)
    vedatsan = models.ForeignKey(VeDatSan,on_delete=models.CASCADE)
    courtStaff = models.ForeignKey(CourtStaff, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.maHoaDon} {self.ngayTao}"