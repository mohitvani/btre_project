# Generated by Django 2.2.5 on 2019-09-12 09:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0003_auto_20190911_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 12, 2, 2, 9, 852305)),
        ),
    ]
