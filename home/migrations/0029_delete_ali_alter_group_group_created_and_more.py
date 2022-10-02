# Generated by Django 4.1 on 2022-09-12 11:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_ali_alter_group_group_created_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ali',
        ),
        migrations.AlterField(
            model_name='group',
            name='group_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 12, 11, 29, 43, 859320, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='page',
            name='page_modified',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 12, 11, 29, 43, 859836, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='page',
            name='page_time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 12, 11, 29, 43, 859805, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 12, 11, 29, 43, 861644, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='story',
            name='story_time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 12, 11, 29, 43, 860521, tzinfo=datetime.timezone.utc)),
        ),
    ]
