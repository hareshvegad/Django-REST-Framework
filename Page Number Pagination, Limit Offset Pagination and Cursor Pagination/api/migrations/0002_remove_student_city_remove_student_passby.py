# Generated by Django 4.2.1 on 2023-12-24 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='city',
        ),
        migrations.RemoveField(
            model_name='student',
            name='passby',
        ),
    ]
