# Generated by Django 2.2 on 2021-10-14 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IoT_Health_Be', '0012_patient_patient_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vitalsigns',
            name='updated_at',
        ),
    ]