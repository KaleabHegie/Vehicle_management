# Generated by Django 4.2.3 on 2023-07-23 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicle_assignment', '0008_alter_registry_driver_alter_registry_employee_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
    ]