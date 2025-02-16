# Generated by Django 5.1.4 on 2025-02-16 13:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BCourt', '0005_court_price_san_numsan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Duong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sonha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='court',
            name='address',
        ),
        migrations.CreateModel(
            name='Phuong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('duong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BCourt.duong')),
            ],
        ),
        migrations.CreateModel(
            name='Quan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phuong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BCourt.phuong')),
            ],
        ),
        migrations.AddField(
            model_name='duong',
            name='sonha',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BCourt.sonha'),
        ),
        migrations.CreateModel(
            name='Tinh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BCourt.quan')),
            ],
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.AddField(
            model_name='court',
            name='Address',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='BCourt.tinh'),
            preserve_default=False,
        ),
    ]
