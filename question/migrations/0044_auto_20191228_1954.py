# Generated by Django 3.0 on 2019-12-28 16:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('question', '0043_auto_20191216_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 28, 16, 54, 49, 653318, tzinfo=utc),
                                       verbose_name='Дата ответа'),
        ),
        migrations.AlterField(
            model_name='article',
            name='date_published',
            field=models.DateTimeField(db_index=True,
                                       default=datetime.datetime(2019, 12, 28, 16, 54, 49, 649500, tzinfo=utc),
                                       verbose_name='Дата публикации'),
        ),
    ]
