# Generated by Django 4.2.3 on 2023-07-22 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicle_assignment', '0007_remove_registry_vehicle_alter_registry_driver_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registry',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Vehicle_assignment.driver'),
        ),
        migrations.AlterField(
            model_name='registry',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Vehicle_assignment.employee'),
        ),
        migrations.AlterField(
            model_name='registry',
            name='officer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Vehicle_assignment.officer'),
        ),
    ]
