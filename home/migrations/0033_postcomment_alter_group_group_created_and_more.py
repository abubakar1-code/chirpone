# Generated by Django 4.1 on 2022-09-12 11:53

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_alter_group_group_created_alter_page_page_modified_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('comment_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('comment_text', models.TextField()),
                ('comment_created', models.DateTimeField(default=datetime.datetime(2022, 9, 12, 11, 53, 3, 452246, tzinfo=datetime.timezone.utc))),
            ],
        ),
        migrations.AlterField(
            model_name='group',
            name='group_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 12, 11, 53, 3, 452727, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='page',
            name='page_modified',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 12, 11, 53, 3, 453232, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='page',
            name='page_time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 12, 11, 53, 3, 453204, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 12, 11, 53, 3, 454892, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='postuser',
            name='post_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 12, 11, 53, 3, 451855, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='story',
            name='story_time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 12, 11, 53, 3, 453950, tzinfo=datetime.timezone.utc)),
        ),
        migrations.DeleteModel(
            name='comment',
        ),
        migrations.AddField(
            model_name='postcomment',
            name='comment_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.postuser'),
        ),
        migrations.AddField(
            model_name='postcomment',
            name='comment_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]