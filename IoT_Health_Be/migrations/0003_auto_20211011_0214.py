# Generated by Django 2.2 on 2021-10-11 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IoT_Health_Be', '0002_auto_20211006_0605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vitalsigns',
            name='blood_pressure',
            field=models.CharField(max_length=32),
        ),
    ]
