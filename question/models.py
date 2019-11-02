# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.shortcuts import render


class Tags(models.Model):
    name = models.CharField(max_length=255, verbose_name="Тег", default="TechnoPark")
    count = models.IntegerField(verbose_name="Число упоминаний")

    def __str__(self):
        return '{}_{}'.format(self.name, self.count)


class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')
    birthday = models.DateField(verbose_name='День рождения')

    def __str__(self):
        return '{}_{}'.format(self.name, self.rating)

    # "красивое" название модели
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class ArticleManager(models.Manager):
    def new_published(self):
        return self.filter(
            is_published=True,
            date_published__lt=datetime.now(),
        ).order_by("-date_published")

    def best_published(self):
        return self.filter(is_published=True, date_published__lt=datetime.now()).order_by("-like")

    def by_tag(self,tag):
        return self.filter(is_published=True,date_published__lt=datetime.now(),tags__name=tag)

class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    date_published = models.DateTimeField(verbose_name='Дата публикации')
    is_published = models.BooleanField(verbose_name='Опубликовано')
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
    )
    like = models.IntegerField(verbose_name="Число лайков", default=0)
    dislike = models.IntegerField(verbose_name="Число дизлайков", default=0)
    tags = models.ManyToManyField(Tags)

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

    like = models.IntegerField(verbose_name="Число лайков", default=0)
    dislike = models.IntegerField(verbose_name="Число дизлайков", default=0)

    text = models.TextField(verbose_name='Текст ответа')
    date_published = models.DateTimeField(verbose_name='Дата ответа')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    objects = AnswerManager()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class Like(models.Model):
    author=models.CharField(max_length=255,verbose_name="Автор лайка",default="admin")
    is_set=models.BooleanField(verbose_name="Поставлен ли лайк",default=False)


class Dislike(models.Model):
    author = models.CharField(max_length=255,verbose_name="Автор дизлайка", default="admin")
    is_set = models.BooleanField(verbose_name="Поставлен ли дизлайк", default=False)


