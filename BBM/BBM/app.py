from django.db import models

class VIPCustomer(models.Model):
    name = models.CharField(max_length=255)
    booked_hours = models.IntegerField()
    discount = models.FloatField()

    def __str__(self):
        return self.name

class Payment(models.Model):
    customer = models.CharField(max_length=255)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.customer} - {self.amount} VNĐ"

class Revenue(models.Model):
    date = models.DateField()
    total_revenue = models.DecimalField(max_digits=15, decimal_places=2)
    total_bookings = models.IntegerField()

    def __str__(self):
        return f"{self.date} - {self.total_revenue} VNĐ"

class Court(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    open_time = models.TimeField()
    close_time = models.TimeField()
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='court_images/')

    def __str__(self):
        return self.name
