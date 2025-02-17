# Generated by Django 5.0.11 on 2025-02-17 11:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('BBooking', '0001_initial'),
        ('BCourt', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='checkin',
            name='courtstaff',
            field=models.ForeignKey(limit_choices_to={'role': 'courtstaff'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='timeslot',
            name='san',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BCourt.san'),
        ),
        migrations.AddField(
            model_name='vedatsan',
            name='customer',
            field=models.ForeignKey(limit_choices_to={'role': 'customer'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vedatsan',
            name='timeslot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BBooking.timeslot'),
        ),
        migrations.AddField(
            model_name='checkin',
            name='vedatsan',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='checkins', to='BBooking.vedatsan'),
        ),
        migrations.AddField(
            model_name='voucher',
            name='court',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BCourt.court'),
        ),
        migrations.AddField(
            model_name='vedatsan',
            name='voucher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BBooking.voucher'),
        ),
        migrations.AlterUniqueTogether(
            name='vedatsan',
            unique_together={('date', 'timeslot')},
        ),
    ]
