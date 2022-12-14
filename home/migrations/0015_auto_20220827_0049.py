# Generated by Django 3.2.14 on 2022-08-27 07:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20220826_2330'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackPost',
            fields=[
                ('back_post_id', models.AutoField(primary_key=True, serialize=False)),
                ('back_post_img', models.FileField(upload_to='post_back')),
            ],
        ),
        migrations.CreateModel(
            name='Gif',
            fields=[
                ('gif_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('gif_url', models.URLField(max_length=400)),
            ],
        ),
        migrations.AlterField(
            model_name='group',
            name='group_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 27, 7, 49, 11, 355295, tzinfo=utc)),
        ),
    ]
