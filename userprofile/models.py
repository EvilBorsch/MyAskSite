# -*- coding:utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='question/static/images/avatars', verbose_name='Изображение',
                               default='question/static/question/base/default.jpeg')

    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.user.username
