from django.db import models
from BCourt.models import Court, San
from BUser.models import User, CourtStaff

# Create your models here.
class TimeSlot(models.Model):
    timeslot = models.DateTimeField()
    
class TimeSlotCourt(models.Model):
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    timeslot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["court", "timeslot"], name="unique_Timeslot")
        ]
    def __str__(self):
        return f"{self.timeslot}"

class VeDatSan(models.Model):
    maVe = models.CharField(default='',max_length=10, primary_key=True)
    thanhToan = models.BooleanField(default=True)
    san = models.ManyToManyField(San)
    timeslot = models.ManyToManyField(TimeSlot)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role':'Customer'})
    def __str__(self):
        return f"{self.maVe}"

class HoaDon(models.Model):
    maHoaDon = models.CharField(default='',max_length=10, primary_key=True)
    tongTien = models.IntegerField(default=0)
    ngayTao = models.DateTimeField()
    note = models.CharField(default='',max_length=255)
    vedatsan = models.OneToOneField(VeDatSan,on_delete=models.CASCADE)
    courtStaff = models.ForeignKey(CourtStaff, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.maHoaDon} {self.ngayTao}"