# Generated by Django 2.2.5 on 2019-09-11 13:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0002_auto_20190911_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 11, 6, 14, 35, 583603)),
        ),
    ]
