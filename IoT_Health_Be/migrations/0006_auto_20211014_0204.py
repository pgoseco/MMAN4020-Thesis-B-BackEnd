# Generated by Django 2.2 on 2021-10-14 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IoT_Health_Be', '0005_auto_20211014_0133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='created_at',
            new_name='registered_at',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='created_at',
            new_name='registered_at',
        ),
    ]