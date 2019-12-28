# Generated by Django 3.0 on 2019-12-16 13:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('question', '0036_auto_20191215_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='answer',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 16, 13, 42, 58, 474626, tzinfo=utc),
                                       verbose_name='Дата ответа'),
        ),
        migrations.AlterField(
            model_name='article',
            name='date_published',
            field=models.DateTimeField(db_index=True,
                                       default=datetime.datetime(2019, 12, 16, 13, 42, 58, 472013, tzinfo=utc),
                                       verbose_name='Дата публикации'),
        ),
    ]