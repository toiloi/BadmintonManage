from django.db import models
from BCourt.models import Court, San
from BUser.models import User
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class TimeSlot(models.Model):
    timeslot = models.TimeField(primary_key=True)
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.timeslot}"
    
class Flag(models.Model):
    san = models.ForeignKey(San, on_delete=models.CASCADE)
    timeslot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    date = models.DateField()
    class Meta:
        unique_together = ('date', 'timeslot')


class Voucher(models.Model):
    voucher=models.CharField(max_length=255,primary_key=True)
    
    court=models.ForeignKey(Court, on_delete=models.CASCADE)
    percent=models.IntegerField(default=5,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    def __str__(self):
        return f"{self.voucher} {self.court.maCourt} - {self.percent}"

class VeDatSan(models.Model):
    CHECKIN_CHOICES = [
        ("chuacheckin", "Chưa check-in"),
        ("dacheckin", "Đã check-in"),
    ]
    TYPE_CHOICES = [
        ("codinh", "Cố định"),
        ("theongay", "Theo ngày"),
        ("linhhoat", "Linh hoạt"),
    ]
    maVe=models.AutoField(primary_key=True)
    flag = models.ForeignKey(Flag, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'customer'})
    tongTien = models.IntegerField(default=0)
    ngayTao = models.DateTimeField(auto_now_add=True)
    voucher=models.ForeignKey(Voucher, on_delete=models.CASCADE, blank=True, null=True)
    checkin = models.CharField(
        max_length=20, choices=CHECKIN_CHOICES, default="chuacheckin"
    )
    type = models.CharField(max_length=8,choices=TYPE_CHOICES, default="codinh")

    def mark_as_checked_in(self):
        """Cập nhật trạng thái check-in khi nhân viên check-in."""
        self.checkin = "dacheckin"
        self.save()

    def __str__(self):
        return f"{self.flag.date} {self.flag.timeslot} - {self.checkin}"

class CheckIn(models.Model):
    vedatsan = models.OneToOneField(VeDatSan, on_delete=models.CASCADE, related_name="checkins")
    courtstaff = models.ForeignKey("BUser.User", on_delete=models.CASCADE, limit_choices_to={'role': 'courtstaff'})
    timeCheckin = models.DateTimeField(default=now)

    def __str__(self):
        return f"Check-in: {self.vedatsan} bởi {self.courtstaff.username} lúc {self.timeCheckin}"
    
class flexTime(models.Model):
    customer=models.ForeignKey("BUser.User", on_delete=models.CASCADE, limit_choices_to={'role': 'customer'})
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    time=models.IntegerField(default=0,validators=[MinValueValidator(0)])
    class Meta:
        unique_together = ('customer', 'court')
    def __str__(self):
        return f"{self.customer.username} {self.court.name} {self.time}"
    

    