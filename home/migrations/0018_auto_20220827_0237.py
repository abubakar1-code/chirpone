# Generated by Django 3.2.14 on 2022-08-27 09:37

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20220827_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 27, 9, 37, 18, 524593, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 27, 9, 37, 18, 524593, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='PostMedia',
            fields=[
                ('post_media_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_media_media', models.FileField(upload_to='post_media')),
                ('post_media_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.post')),
            ],
        ),
    ]