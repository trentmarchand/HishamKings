# Generated by Django 4.0.3 on 2022-05-01 17:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_bet_status_alter_bet_bet_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='bet_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 1, 13, 57, 46, 277443)),
        ),
    ]
