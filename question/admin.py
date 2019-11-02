from django.contrib import admin
from question import models
# Register your models here.



admin.site.register(models.Author)
admin.site.register(models.Article)
admin.site.register(models.Answer)
admin.site.register(models.Tags)
admin.site.register(models.Like)
admin.site.register(models.Dislike)