# Generated by Django 2.2 on 2021-10-14 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IoT_Health_Be', '0016_patient_unique_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='vitalsigns',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patient_vitalsign', to='IoT_Health_Be.Patient'),
        ),
    ]
