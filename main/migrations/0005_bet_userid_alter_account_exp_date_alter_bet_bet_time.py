# Generated by Django 4.0.3 on 2022-04-28 16:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_alter_bet_bet_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='userID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='exp_date',
            field=models.DateField(default=datetime.date(2022, 4, 28)),
        ),
        migrations.AlterField(
            model_name='bet',
            name='bet_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 28, 12, 53, 8, 94739), editable=False),
        ),
    ]
