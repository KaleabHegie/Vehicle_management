# Generated by Django 4.2.3 on 2023-07-24 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicle_assignment', '0009_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vehicle_assignment.employee')),
            ],
        ),
    ]