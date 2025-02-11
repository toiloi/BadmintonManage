from django.db import models

# Create your models here.
class Address(models.Model):
    soNha = models.CharField(max_length=255,default='')
    xa = models.CharField(max_length=255,default='')
    huyen = models.CharField(max_length=255,default='')
    tinh = models.CharField(max_length=255,default='')
    quocGia = models.CharField(max_length=255,default='')
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["soNha", "xa", "huyen", "tinh", "quocGia"], name="unique_address")
        ]
    def __str__(self):
        return f"{self.soNha} {self.huyen} {self.tinh} {self.quocGia}"

class Court(models.Model):
    courtManager = models.ForeignKey("BUser.User", on_delete=models.CASCADE, limit_choices_to={'role':'courtmanager'})
    maCourt = models.CharField(default='',max_length=10, primary_key=True)
    name = models.CharField(default='',max_length=255)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    descreption = models.CharField(default='',max_length=255, null=True, blank= True)
    img=models.ImageField(upload_to="images/")
    def __str__(self):
        return f"{self.maCourt} {self.name} {self.address}"

class San(models.Model):
    maSan = models.CharField(default='',max_length=10, primary_key=True)
    tinhTrang = models.BooleanField(default=True)
    court=models.ForeignKey(Court, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.maSan} {self.tinhTrang}"