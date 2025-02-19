from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
# Create your models here.

class Address(models.Model):
    soNha=models.CharField(max_length=100)
    duong=models.CharField(max_length=100)
    phuong=models.CharField(max_length=100)
    quan=models.CharField(max_length=100)
    tinh=models.CharField(max_length=100)
    class Meta:
        unique_together = ['soNha', 'duong', 'phuong', 'quan', 'tinh']
    def __str__(self):
        return f"{self.soNha} {self.duong} {self.phuong} {self.quan} {self.tinh} "

class Court(models.Model):
    courtManager = models.ForeignKey("BUser.User", on_delete=models.CASCADE, limit_choices_to={'role':'courtmanager'})
    maCourt = models.CharField(default='',max_length=10, primary_key=True)
    name = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    price = models.IntegerField(validators=[MinValueValidator(10000)])
    description = models.CharField(default='',max_length=255, null=True, blank= True)
    img = models.ImageField(upload_to="images/", verbose_name="Hình ảnh sân")
    courtStaff=models.ManyToManyField("BUser.User", limit_choices_to={'role':'courtstaff'}, related_name="staffed_courts", blank=True)
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
    court=models.ForeignKey(Court, on_delete=models.CASCADE)
    def __str__(self):
        return f"Sân {self.numSan}"