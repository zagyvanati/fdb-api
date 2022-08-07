# Generated by Django 4.0.6 on 2022-08-07 07:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_page_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 8, 7, 7, 55, 6, 877304, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='edited',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
