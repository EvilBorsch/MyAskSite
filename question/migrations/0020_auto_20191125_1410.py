# Generated by Django 2.2.6 on 2019-11-25 14:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('question', '0019_auto_20191125_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 25, 14, 10, 44, 569218, tzinfo=utc),
                                       verbose_name='Дата публикации'),
        ),
    ]
