# Generated by Django 2.2.6 on 2019-11-02 11:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('question', '0009_dislike_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dislike',
            name='author',
            field=models.CharField(default='admin', max_length=255, verbose_name='Автор дизлайка'),
        ),
        migrations.AlterField(
            model_name='dislike',
            name='is_set',
            field=models.BooleanField(default=False, verbose_name='Поставлен ли дизлайк'),
        ),
    ]
