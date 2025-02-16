from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
# Create your models here.

class Sonha (models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    def __str__(self):
        return f"{self.name}"

class Duong (models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    sonha = models.ForeignKey(Sonha, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}"

class Phuong (models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    duong = models.ForeignKey(Duong, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}"

class Quan (models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    phuong = models.ForeignKey(Phuong, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}"

class Tinh(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    quan = models.ForeignKey(Quan, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.quan.phuong.duong.sonha.name} {self.quan.phuong.duong.name} P.{self.quan.phuong.name} Q.{self.quan.name} {self.name}"


class Court(models.Model):
    courtManager = models.ForeignKey("BUser.User", on_delete=models.CASCADE, limit_choices_to={'role':'courtmanager'})
    maCourt = models.CharField(default='',max_length=10, primary_key=True)
    name = models.CharField(max_length=100)
    address = models.OneToOneField(Tinh, on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField()
    description = models.CharField(default='',max_length=255, null=True, blank= True)
    img = models.ImageField(upload_to="images/", verbose_name="Hình ảnh sân")
    rateAvr = models.FloatField(default=0.0)  # Trung bình rating

    def update_rating(self):
        avg_rating = self.rating_set.aggregate(Avg("rate"))["rate__avg"]  # Tính trung bình
        self.rateAvr = avg_rating if avg_rating is not None else 0.0
        self.save()
    def __str__(self):
        return f"{self.maCourt} {self.name}"
    
class Rating(models.Model):
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    customer = models.ForeignKey("BUser.User", on_delete=models.CASCADE, limit_choices_to={'role': 'customer'})
    rate = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    class Meta:
        unique_together = ('court', 'customer')
    def __str__(self):
        return f"{self.customer.username} - {self.rate}"
    
@receiver(post_save, sender=Rating)
@receiver(post_delete, sender=Rating)
def update_court_rating(sender, instance, **kwargs):
    instance.court.update_rating()

class San(models.Model):
    maSan = models.CharField(default='',max_length=10, primary_key=True)
    numSan = models.IntegerField()
    tinhTrang = models.BooleanField(default=True)
    court=models.ForeignKey(Court, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.maSan} {self.tinhTrang}"