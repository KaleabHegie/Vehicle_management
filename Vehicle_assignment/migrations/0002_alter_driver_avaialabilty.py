# Generated by Django 4.2.3 on 2023-07-20 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicle_assignment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='avaialabilty',
            field=models.BooleanField(default=True),
        ),
    ]
