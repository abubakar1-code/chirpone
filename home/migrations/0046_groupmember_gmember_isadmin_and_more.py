# Generated by Django 4.1 on 2022-09-19 04:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0045_groupmember_gmember_group_groupmember_gmember_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupmember',
            name='gmember_isadmin',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='addfriend',
            name='addfreind_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 19, 4, 58, 14, 107234, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='addfriend',
            name='addfreind_updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 19, 4, 58, 14, 107255, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='group_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 19, 4, 58, 14, 107900, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='group',
            name='group_updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 19, 4, 58, 14, 107920, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='groupmember',
            name='gmember_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 19, 4, 58, 14, 108575, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='groupmember',
            name='gmember_updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 19, 4, 58, 14, 108595, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='page',
            name='page_modified',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 19, 4, 58, 14, 109436, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='page',
            name='page_time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 19, 4, 58, 14, 109387, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 19, 4, 58, 14, 113498, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='comment_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 19, 4, 58, 14, 105811, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='postlike',
            name='like_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 19, 4, 58, 14, 106481, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='postuser',
            name='post_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 19, 4, 58, 14, 105160, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 19, 4, 58, 14, 104262, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 19, 4, 58, 14, 104289, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='story_time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 19, 4, 58, 14, 110555, tzinfo=datetime.timezone.utc)),
        ),
    ]
