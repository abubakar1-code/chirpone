# Generated by Django 3.2.14 on 2022-08-26 09:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20220826_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 26, 9, 23, 7, 552985, tzinfo=utc)),
        ),
    ]
