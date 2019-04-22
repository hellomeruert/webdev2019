# Generated by Django 2.2 on 2019-04-12 11:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190409_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(default='in process', max_length=50),
        ),
    ]
