# Generated by Django 4.0.3 on 2022-05-01 18:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_bet_bet_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='bet_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 1, 14, 4, 1, 644439)),
        ),
    ]
