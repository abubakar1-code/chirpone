# Generated by Django 4.1 on 2022-09-13 10:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_profile_profile_cover_alter_group_group_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 13, 10, 10, 35, 84456, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='page',
            name='page_modified',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 13, 10, 10, 35, 84948, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='page',
            name='page_time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 13, 10, 10, 35, 84917, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 13, 10, 10, 35, 86538, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='comment_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 13, 10, 10, 35, 83570, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='postlike',
            name='like_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 13, 10, 10, 35, 83965, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='postuser',
            name='post_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 13, 10, 10, 35, 83186, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_activities',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_addfriendlink',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_afflicationcourt',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_favoraitbooks',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_favoraitmovies',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_favoraitmusics',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_favoraitquotes',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_favoraittvshows',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_intrests',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_notesbyuserlink',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_notescourts',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pictuersbyuserlink',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pictuersofuserlink',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_politicalviews',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_postonuserlink',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_profilelink',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_religion',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_schoolcourt',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_sendmessagelink',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_significantid',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_wallcourt',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_workplacecourt',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='story_time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 13, 10, 10, 35, 85595, tzinfo=datetime.timezone.utc)),
        ),
    ]
