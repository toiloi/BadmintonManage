from django.db import models
class Member(models.Model):
    account=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
