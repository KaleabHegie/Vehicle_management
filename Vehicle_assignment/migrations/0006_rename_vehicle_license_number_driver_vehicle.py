# Generated by Django 4.2.3 on 2023-07-21 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicle_assignment', '0005_alter_slider_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='driver',
            old_name='Vehicle_license_number',
            new_name='vehicle',
        ),
    ]
