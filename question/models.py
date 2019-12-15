# -*- coding: utf-8 -*-
from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from userprofile.models import UserProfile


class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя', unique=True)
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')

    def __str__(self):
        return '{}_{}'.format(self.name, self.rating)

    # "красивое" название модели
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'




class Tags(models.Model):
    name = models.CharField(max_length=255, verbose_name="Тег", default="TechnoPark", db_index=True)
    count = models.IntegerField(verbose_name="Число упоминаний", default=0)

    def __str__(self):
        return '{}_{}'.format(self.name, self.count)


class ArticleManager(models.Manager):
    def new_published(self):
        return self.filter(
            is_published=True,
            date_published__lt=datetime.now(tz=timezone.utc),
        ).order_by("-date_published")

    def best_published(self):
        test = list(self.filter(is_published=True, date_published__lt=datetime.now(tz=timezone.utc)))
        test = sorted(test, key=lambda x: x.like.count(), reverse=True)
        return test

    def by_tag(self, tag):
        return self.filter(is_published=True, date_published__lt=datetime.now(tz=timezone.utc), tags__name=tag)


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    date_published = models.DateTimeField(verbose_name='Дата публикации', default=datetime.now(tz=timezone.utc),
                                          db_index=True)
    is_published = models.BooleanField(verbose_name='Опубликовано', default=True, blank=True)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
    )

    like = models.ManyToManyField(UserProfile, related_name="Article_like", blank=True)
    dislike = models.ManyToManyField(UserProfile, related_name="Article_dislike", blank=True)
    tags = models.ManyToManyField(Tags, blank=True)

    objects = ArticleManager()  # model manager

    def __str__(self):
        return self.title

    # используется для генерации классов (красивое обозначение сущностей)
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        index_together = [('title', 'text')]
        unique_together = [('title', 'text')]


class AnswerManager(models.Manager):
    def by_question(self, id):
        return self.filter(question=id)


class Answer(models.Model):
    question = models.ForeignKey(Article, on_delete=models.CASCADE)

    like = models.ManyToManyField(UserProfile, related_name="Answer_like", blank=True)
    dislike = models.ManyToManyField(UserProfile, related_name="Answer_dislike", blank=True)

    text = models.TextField(verbose_name='Текст ответа')
    date_published = models.DateTimeField(verbose_name='Дата ответа', default=datetime.now(tz=timezone.utc))
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    objects = AnswerManager()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
