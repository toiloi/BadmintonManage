from django.db import models
from BCourt.models import Court, San
from BUser.models import User, CourtStaff
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class TimeSlot(models.Model):
    timeslot = models.TimeField(primary_key=True)
    def __str__(self):
        return f"{self.timeslot}"


class VeDatSan(models.Model):
    thanhToan = models.BooleanField(default=True)
    san = models.ForeignKey(San, on_delete=models.CASCADE)
    timeslot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    date = models.DateField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role':'customer'})
    class Meta:
        unique_together = ('san', 'date', 'timeslot')   
    def __str__(self):
        return f"{self.san} {self.date} {self.timeslot} {self.customer}"

class HoaDon(models.Model):
    maHoaDon = models.CharField(default='',max_length=10, primary_key=True)
    tongTien = models.IntegerField(default=0)
    ngayTao = models.DateTimeField()
    vedatsan = models.OneToOneField(VeDatSan,on_delete=models.CASCADE)
    courtStaff = models.ForeignKey(CourtStaff, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return f"{self.maHoaDon} {self.ngayTao}"
    
class Voucher(models.Model):
    voucher=models.CharField(max_length=255)
    court=models.ForeignKey(Court, on_delete=models.CASCADE)
    percent=models.IntegerField(default=5,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    def __str__(self):
        return f"{self.voucher} {self.court.maCourt} - {self.percent}"
