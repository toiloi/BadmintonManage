from django.db import models
# Create your models here.

class Sonha (models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"

class Duong (models.Model):
    name = models.CharField(max_length=100)
    sonha = models.ForeignKey(Sonha, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}"

class Phuong (models.Model):
    name = models.CharField(max_length=100)
    duong = models.ForeignKey(Duong, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}"

class Quan (models.Model):
    name = models.CharField(max_length=100)
    phuong = models.ForeignKey(Phuong, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}"

class Tinh(models.Model):
    name = models.CharField(max_length=100)
    quan = models.ForeignKey(Quan, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

class Court(models.Model):
    courtManager = models.ForeignKey("BUser.User", on_delete=models.CASCADE, limit_choices_to={'role':'courtmanager'})
    maCourt = models.CharField(default='',max_length=10, primary_key=True)
    name = models.CharField(max_length=100)
    address = models.OneToOneField(Tinh, on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField()
    description = models.CharField(default='',max_length=255, null=True, blank= True)
    img = models.ImageField(upload_to="images/", verbose_name="Hình ảnh sân")
    def __str__(self):
        return f"{self.maCourt} {self.name}"

class San(models.Model):
    maSan = models.CharField(default='',max_length=10, primary_key=True)
    numSan = models.IntegerField()
    tinhTrang = models.BooleanField(default=True)
    court=models.ForeignKey(Court, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.maSan} {self.tinhTrang}"