# Generated by Django 2.2.6 on 2019-10-17 11:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0009_auto_20191017_1123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='penalty',
            new_name='penalty_per_day',
        ),
        migrations.AlterField(
            model_name='record',
            name='date_of_return',
            field=models.DateField(default=datetime.datetime(2019, 10, 24, 11, 25, 16, 988859)),
        ),
        migrations.AlterField(
            model_name='record',
            name='issue_date',
            field=models.DateField(default=datetime.datetime(2019, 10, 17, 11, 25, 16, 988835)),
        ),
    ]
