# Generated by Django 2.2.6 on 2019-11-01 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_article_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='dislike',
            field=models.IntegerField(default=0, verbose_name='Число дизлайков'),
        ),
    ]