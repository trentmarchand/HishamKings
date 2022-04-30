# Generated by Django 4.0.3 on 2022-04-30 08:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0011_remove_account_paymentid_account_userid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentmethod',
            name='accountID',
        ),
        migrations.AddField(
            model_name='paymentmethod',
            name='amount',
            field=models.IntegerField(default=0.0),
        ),
        migrations.AddField(
            model_name='paymentmethod',
            name='userID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bet',
            name='bet_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 30, 4, 28, 21, 404601), editable=False),
        ),
        migrations.AlterField(
            model_name='paymentmethod',
            name='exp_date',
            field=models.DateField(default=datetime.date(2022, 4, 30)),
        ),
    ]