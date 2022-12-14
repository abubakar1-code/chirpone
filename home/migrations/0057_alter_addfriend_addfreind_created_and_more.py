# Generated by Django 4.1 on 2022-09-24 07:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0056_alter_addfriend_addfreind_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addfriend',
            name='addfreind_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 24, 7, 4, 34, 152319, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='addfriend',
            name='addfreind_updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 24, 7, 4, 34, 152345, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='blockuser',
            name='blockuser_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 24, 7, 4, 34, 152764, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='blockuser',
            name='blockuser_update',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 24, 7, 4, 34, 152777, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='group',
            name='group_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 24, 7, 4, 34, 153212, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='group',
            name='group_updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 24, 7, 4, 34, 153224, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='groupmember',
            name='gmember_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 24, 7, 4, 34, 153641, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='groupmember',
            name='gmember_updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 24, 7, 4, 34, 153653, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='mchat',
            name='mchat_theme',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.mchattheme'),
        ),
        migrations.AlterField(
            model_name='mchatsms',
            name='sms_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 24, 7, 4, 34, 154883, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='page',
            name='page_modified',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 24, 7, 4, 34, 156648, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='page',
            name='page_time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 24, 7, 4, 34, 156591, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 24, 7, 4, 34, 159134, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='comment_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 24, 7, 4, 34, 151479, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='postlike',
            name='like_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 24, 7, 4, 34, 151876, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='postuser',
            name='post_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 24, 7, 4, 34, 150942, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 24, 7, 4, 34, 150411, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 24, 7, 4, 34, 150428, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='story_time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 24, 7, 4, 34, 157787, tzinfo=datetime.timezone.utc)),
        ),
    ]
