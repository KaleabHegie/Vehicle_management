# Generated by Django 4.2.3 on 2023-07-21 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicle_assignment', '0003_remove_vehicle_avaialabilty'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ServiceDescription',
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
