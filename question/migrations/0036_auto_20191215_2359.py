# Generated by Django 3.0 on 2019-12-15 20:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('question', '0035_auto_20191215_2356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='author',
        ),
        migrations.AlterField(
            model_name='answer',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 15, 20, 59, 13, 807095, tzinfo=utc),
                                       verbose_name='Дата ответа'),
        ),
        migrations.AlterField(
            model_name='article',
            name='date_published',
            field=models.DateTimeField(db_index=True,
                                       default=datetime.datetime(2019, 12, 15, 20, 59, 13, 804591, tzinfo=utc),
                                       verbose_name='Дата публикации'),
        ),
        migrations.DeleteModel(
            name='Dislike',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]