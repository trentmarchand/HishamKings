# Generated by Django 4.0.3 on 2022-03-26 22:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='bet_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 26, 18, 13, 59, 898673), editable=False),
        ),
    ]
