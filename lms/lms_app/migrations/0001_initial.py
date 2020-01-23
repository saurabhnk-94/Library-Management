# Generated by Django 2.2.6 on 2019-10-16 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('library_name', models.CharField(max_length=50)),
                ('library_address', models.CharField(max_length=150)),
                ('library_location', models.CharField(blank=True, max_length=100)),
                ('library_mail', models.EmailField(blank=True, max_length=254)),
            ],
        ),
    ]
