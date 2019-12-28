# Generated by Django 3.0 on 2019-12-16 13:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('question', '0038_auto_20191216_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 16, 13, 55, 3, 477427, tzinfo=utc),
                                       verbose_name='Дата ответа'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='date_published',
            field=models.DateTimeField(db_index=True,
                                       default=datetime.datetime(2019, 12, 16, 13, 55, 3, 474942, tzinfo=utc),
                                       verbose_name='Дата публикации'),
        ),
    ]