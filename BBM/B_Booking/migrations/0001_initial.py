# Generated by Django 5.0.11 on 2025-02-10 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HoaDon',
            fields=[
                ('maHoaDon', models.CharField(default='', max_length=10, primary_key=True, serialize=False)),
                ('tongTien', models.IntegerField(default=0)),
                ('ngayTao', models.DateTimeField()),
                ('note', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeslot', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlotCourt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='VeDatSan',
            fields=[
                ('maVe', models.CharField(default='', max_length=10, primary_key=True, serialize=False)),
                ('thanhToan', models.BooleanField(default=True)),
            ],
        ),
    ]
