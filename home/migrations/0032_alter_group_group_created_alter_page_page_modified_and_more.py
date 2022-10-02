# Generated by Django 4.1 on 2022-09-12 11:51

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_postuser_post_creater_alter_group_group_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 12, 11, 51, 27, 672076, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='page',
            name='page_modified',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 12, 11, 51, 27, 672572, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='page',
            name='page_time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 12, 11, 51, 27, 672545, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 12, 11, 51, 27, 674235, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='postuser',
            name='post_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 12, 11, 51, 27, 671275, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='story',
            name='story_time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 12, 11, 51, 27, 673316, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('comment_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('comment_text', models.TextField()),
                ('comment_created', models.DateTimeField(default=datetime.datetime(2022, 9, 12, 11, 51, 27, 671658, tzinfo=datetime.timezone.utc))),
                ('comment_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.postuser')),
                ('comment_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
