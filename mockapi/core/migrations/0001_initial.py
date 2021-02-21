# Generated by Django 3.1.7 on 2021-02-21 09:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=70)),
                ('generate_date', models.DateTimeField(default=datetime.datetime(2021, 2, 21, 16, 59, 11, 155942))),
                ('expired_date', models.DateTimeField(default=datetime.datetime(2021, 3, 13, 16, 59, 11, 155942))),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
