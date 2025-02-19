# Generated by Django 5.1.3 on 2025-02-19 16:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("BBooking", "0001_initial"),
        ("BCourt", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="checkin",
            name="courtstaff",
            field=models.ForeignKey(
                limit_choices_to={"role": "courtstaff"},
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="flag",
            name="san",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="BCourt.san"
            ),
        ),
        migrations.AddField(
            model_name="timeslot",
            name="court",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="BCourt.court"
            ),
        ),
        migrations.AddField(
            model_name="flag",
            name="timeslot",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="BBooking.timeslot"
            ),
        ),
        migrations.AddField(
            model_name="vedatsan",
            name="customer",
            field=models.ForeignKey(
                limit_choices_to={"role": "customer"},
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="vedatsan",
            name="flag",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="BBooking.flag"
            ),
        ),
        migrations.AddField(
            model_name="checkin",
            name="vedatsan",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="checkins",
                to="BBooking.vedatsan",
            ),
        ),
        migrations.AddField(
            model_name="voucher",
            name="court",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="BCourt.court"
            ),
        ),
        migrations.AddField(
            model_name="vedatsan",
            name="voucher",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="BBooking.voucher",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="flag",
            unique_together={("date", "timeslot")},
        ),
    ]
