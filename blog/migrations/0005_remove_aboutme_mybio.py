# Generated by Django 2.0.13 on 2019-06-15 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_aboutme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutme',
            name='mybio',
        ),
    ]
