# Generated by Django 2.0.13 on 2019-06-16 06:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20190616_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='qdate',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
