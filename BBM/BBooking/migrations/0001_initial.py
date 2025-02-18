# Generated by Django 5.0.11 on 2025-02-18 13:43

import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheckIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeCheckin', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('timeslot', models.TimeField(primary_key=True, serialize=False)),
                ('flag', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='VeDatSan',
            fields=[
                ('maVe', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('tongTien', models.IntegerField(default=0)),
                ('ngayTao', models.DateTimeField(auto_now_add=True)),
                ('checkin', models.CharField(choices=[('chuacheckin', 'Chưa check-in'), ('dacheckin', 'Đã check-in')], default='chua_checkin', max_length=20)),
                ('type', models.CharField(choices=[('codinh', 'Cố định'), ('theongay', 'Theo ngày'), ('linhhoat', 'Linh hoạt')], default='codinh', max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voucher', models.CharField(max_length=10)),
                ('percent', models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
    ]
