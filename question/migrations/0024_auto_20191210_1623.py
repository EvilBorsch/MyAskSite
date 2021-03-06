# Generated by Django 3.0 on 2019-12-10 13:23

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('question', '0023_auto_20191203_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 10, 13, 23, 49, 870958, tzinfo=utc),
                                       verbose_name='Дата ответа'),
        ),
        migrations.AlterField(
            model_name='article',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 10, 13, 23, 49, 868221, tzinfo=utc),
                                       verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='dislike',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.Author', unique=True),
        ),
        migrations.AlterField(
            model_name='like',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.Author', unique=True),
        ),
    ]
