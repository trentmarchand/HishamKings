# Generated by Django 4.0.3 on 2022-04-30 02:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0010_account_paymentid_alter_bet_bet_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='paymentID',
        ),
        migrations.AddField(
            model_name='account',
            name='userID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='paymentmethod',
            name='accountID',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='main.account'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='bet',
            name='bet_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 29, 22, 52, 17, 81442), editable=False),
        ),
    ]
