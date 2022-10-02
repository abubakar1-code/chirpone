# Generated by Django 4.1 on 2022-09-13 11:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0038_remove_profile_profile_addfriendlink_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 13, 11, 7, 35, 765678, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='page',
            name='page_modified',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 13, 11, 7, 35, 766217, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='page',
            name='page_time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 13, 11, 7, 35, 766189, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 13, 11, 7, 35, 767808, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='comment_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 13, 11, 7, 35, 764803, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='postlike',
            name='like_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 13, 11, 7, 35, 765190, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='postuser',
            name='post_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 13, 11, 7, 35, 764422, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_aboutme',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_cover',
            field=models.FileField(null=True, upload_to='profile_cover'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.FileField(null=True, upload_to='profile_picture'),
        ),
        migrations.AlterField(
            model_name='story',
            name='story_time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 13, 11, 7, 35, 766867, tzinfo=datetime.timezone.utc)),
        ),
    ]
