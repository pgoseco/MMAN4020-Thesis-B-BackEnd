# Generated by Django 2.2 on 2021-10-14 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IoT_Health_Be', '0007_auto_20211014_0212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vitalsigns',
            name='patients',
        ),
        migrations.DeleteModel(
            name='HistoricalVitalSigns',
        ),
    ]
