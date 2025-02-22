# Generated by Django 4.2.14 on 2024-07-16 10:05

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MissionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mission', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MissionMonitoring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(default=django.utils.timezone.now)),
                ('progress', models.BooleanField(default=False)),
                ('worked_time', models.DurationField(default=datetime.timedelta(0))),
                ('mission_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checklist.missiontype')),
            ],
        ),
    ]
