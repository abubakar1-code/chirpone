# Generated by Django 3.2.14 on 2022-08-25 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20220824_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='group_icon',
            field=models.FileField(default=1, upload_to='group_icon'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_groups',
            field=models.JSONField(default={'groups': []}),
        ),
    ]
