# Generated by Django 3.0 on 2019-12-10 17:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('question', '0031_auto_20191210_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 10, 17, 13, 59, 87200, tzinfo=utc),
                                       verbose_name='Дата ответа'),
        ),
        migrations.AlterField(
            model_name='article',
            name='date_published',
            field=models.DateTimeField(db_index=True,
                                       default=datetime.datetime(2019, 12, 10, 17, 13, 59, 84791, tzinfo=utc),
                                       verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='tags',
            name='name',
            field=models.CharField(db_index=True, default='TechnoPark', max_length=255, verbose_name='Тег'),
        ),
    ]
