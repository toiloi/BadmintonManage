from django.db import models
from BCourt.models import Court, San
from BUser.models import User, CourtStaff
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid

# Create your models here.
class TimeSlot(models.Model):
    timeslot = models.TimeField(primary_key=True)
    san = models.ForeignKey(San, on_delete=models.CASCADE)
    flag = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.timeslot}"

class Voucher(models.Model):
    voucher=models.CharField(max_length=10)
    court=models.ForeignKey(Court, on_delete=models.CASCADE)
    percent=models.IntegerField(default=5,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

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
    timeslot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    date = models.DateField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'customer'})
    tongTien = models.IntegerField(default=0)
    ngayTao = models.DateTimeField(auto_now_add=True)
    voucher=models.ForeignKey(Voucher, on_delete=models.CASCADE, blank=True, null=True)
    checkin = models.CharField(
        max_length=20, choices=CHECKIN_CHOICES, default="chua_checkin"
    )
    type = models.CharField(max_length=8,choices=TYPE_CHOICES, default="codinh")

    class Meta:
        unique_together = ('date', 'timeslot')

    def mark_as_checked_in(self):
        """Cập nhật trạng thái check-in khi nhân viên check-in."""
        self.checkin = "da_checkin"
        self.save()

    def __str__(self):
        return f"{self.date} {self.timeslot} - {self.checkin}"

class CheckIn(models.Model):
    vedatsan = models.OneToOneField(VeDatSan, on_delete=models.CASCADE, related_name="checkins")
    courtstaff = models.ForeignKey("BUser.User", on_delete=models.CASCADE, limit_choices_to={'role': 'courtstaff'})
    timeCheckin = models.DateTimeField(default=now)

    def __str__(self):
        return f"Check-in: {self.vedatsan} bởi {self.courtstaff.username} lúc {self.timeCheckin}"