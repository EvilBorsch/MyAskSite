# Generated by Django 3.0 on 2019-12-10 17:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('question', '0030_auto_20191210_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 10, 17, 11, 53, 889467, tzinfo=utc),
                                       verbose_name='Дата ответа'),
        ),
        migrations.AlterField(
            model_name='article',
            name='date_published',
            field=models.DateTimeField(db_index=True,
                                       default=datetime.datetime(2019, 12, 10, 17, 11, 53, 886695, tzinfo=utc),
                                       verbose_name='Дата публикации'),
        ),
    ]