# Generated by Django 4.0.3 on 2022-05-01 01:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_paymentmethod_accountid_paymentmethod_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='bet_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 30, 21, 41, 28, 337699), editable=False),
        ),
    ]
