# Generated by Django 4.1 on 2022-09-12 11:56

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_postcomment_alter_group_group_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 12, 11, 56, 29, 211682, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='page',
            name='page_modified',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 12, 11, 56, 29, 212259, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='page',
            name='page_time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 12, 11, 56, 29, 212231, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 12, 11, 56, 29, 213998, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='comment_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 12, 11, 56, 29, 210868, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='postuser',
            name='post_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 12, 11, 56, 29, 210480, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='story',
            name='story_time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 12, 11, 56, 29, 212950, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('like_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('like_created', models.DateTimeField(default=datetime.datetime(2022, 9, 12, 11, 56, 29, 211270, tzinfo=datetime.timezone.utc))),
                ('like_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.postuser')),
                ('like_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
