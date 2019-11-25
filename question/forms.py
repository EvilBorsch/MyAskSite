from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.forms import ModelForm
from django import forms

from question.models import Article
from userprofile.models import UserProfile


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text', 'author', 'date_published',
                  'is_published']  # поля которые сохраняем. потом во вьюхе сделаем "from" : ArticleFrom() а в template в каждом поле что пишем в формах гуглить django froms manually

    # тут проверка на чистоту данных(чекай заметки) и фотки в телефоне
    def clean_title(self):
        return ValidationError("Тайтд ")


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

    def clean_username(self):
        username = self.cleaned_data["username"]

        if (username != "yandex"):
            return username
        else:
            raise ValidationError("ban")

    def clean_password(self):
        password = self.cleaned_data["password"]
        return password


class RegisterForm(ModelForm):
    login = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    repeated_password = forms.CharField()
    nickname = forms.CharField()

    class Meta:
        model = UserProfile
        fields = ["avatar"]

    def clean_repeated_password(self):

        if (self.cleaned_data["password"] == self.cleaned_data["repeated_password"]):

            return self.cleaned_data["repeated_password"]
        else:
            raise ValidationError("Пароли не совпадают")

    def clean_nickname(self):
        return self.cleaned_data["nickname"]

    def clean_login(self):
        login = self.cleaned_data["login"]

        if (login != "yandex"):
            return login
        else:
            raise ValidationError("ban")

    def clean_email(self):
        email = self.cleaned_data["email"]
        validate_email(email)
        return email

    def clean_password(self):
        password = self.cleaned_data["password"]
        return password

    def clean_avatar(self):

        try:
            avatar = self.cleaned_data["avatar"]
            print("ya tut")
            return avatar
        except:
            print("test")

