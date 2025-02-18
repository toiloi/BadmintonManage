# Generated by Django 5.1.3 on 2025-02-17 16:37

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DailyStat",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("revenue", models.DecimalField(decimal_places=2, max_digits=10)),
                ("bookings", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="staffRequest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=15)),
                ("date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("transaction_id", models.CharField(max_length=100)),
                ("customer_name", models.CharField(max_length=100)),
                ("date", models.DateField()),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("status", models.CharField(max_length=50)),
            ],
        ),
    ]
