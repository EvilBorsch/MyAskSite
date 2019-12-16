from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect

from question import models
from question.forms import LoginForm, RegisterForm, QuestionForm, AnswerForm
from question.models import Author, Article, Tags
from django.urls import reverse
import json

from django.http import JsonResponse

from userprofile.models import UserProfile
from django import db


def one_question(request, m_id):
    try:
        main_quest = models.Article.objects.get(pk=m_id)
    except (models.Article.DoesNotExist, ValueError):
        return render(request, "./question/404.html")
    answers = models.Answer.objects.by_question(m_id)
    paginated_data = paginate(answers, request)
    form = AnswerForm(author=Author.objects.get(pk=1), question_id=m_id)
    if request.POST:
        aut, _ = Author.objects.get_or_create(name=request.user.username)

        form = AnswerForm(
            author=aut, question_id=m_id, data=request.POST)

        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            print(form.errors)
            rendered_data = {"questions": paginated_data, "main_question": main_quest, "form": form}
            return render(request, "./question/one_question.html", rendered_data)

    rendered_data = {"questions": paginated_data, "main_question": main_quest, "form": form}
    return render(request, "./question/one_question.html", rendered_data)


def index_html(request):
    articles = models.Article.objects.new_published()
    paginated_data = paginate(articles, request)
    rendered_data = {"questions": paginated_data}
    return render(request, "./question/index.html", rendered_data)


def login_html(request):
    if request.method == "POST":
        redirected_path = request.GET["put"]
        form = LoginForm(request.POST)
        if form.is_valid():
            print("OK")
            username = form.clean_username()
            password = form.clean_password()
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(redirected_path)
            else:
                form.add_error(None, 'Неправильный логин или пароль')

                return render(request, "./question/login.html", {"form": form})
        else:

            return render(request, "./question/login.html", {"form": form})
    else:
        form = LoginForm()

        return render(request, "./question/login.html", {"form": form})


def register_html(request):
    if request.method == "POST":
        # print(request.POST)
        form = RegisterForm(request.POST)
        # print(form.cleaned_data)

        if form.is_valid():
            print("OK")
            username = form.clean_login()
            password = form.clean_password()
            email = form.clean_email()
            nickname = form.clean_nickname()
            user = User.objects.create_user(username=username, password=password, email=email)
            user.first_name = nickname
            user.save()

            login(request, user=user)

            return redirect('/')
        else:
            print(form.errors)
            return render(request, "./question/register.html", {"form": form})
    else:
        form = RegisterForm()
        return render(request, "./question/register.html", {"form": form})


def add_question_html(request):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.POST:

        aut, _ = Author.objects.get_or_create(name=request.user.username)

        form = QuestionForm(
            aut, data=request.POST)
        if form.is_valid():
            question = form.save()
            return redirect(
                reverse(
                    "one_question_url", kwargs={'m_id': question.pk}))
        else:
            print(form.errors)
            return render(request, 'question/add_question.html', {
                'form': form,
            })
    else:
        form = QuestionForm(author=Author.objects.get(pk=1))
        return render(request, 'question/add_question.html', {
            'form': form,
        })


def questions_by_tag_html(request, tag="kek"):
    articles = models.Article.objects.by_tag(tag)
    paginated_data = paginate(articles, request)
    rendered_data = {"questions": paginated_data, "m_tag": tag}
    return render(request, "./question/questions_bt_tag.html", rendered_data)


def hot_questions_html(request):
    articles = models.Article.objects.best_published()
    paginated_data = paginate(articles, request)
    rendered_data = {"questions": paginated_data}

    return render(request, "./question/hot_questions.html", rendered_data)


def paginate(objects_list, request):
    paginator = Paginator(list(objects_list), 4)

    page = request.GET.get('page')
    try:
        contacts = paginator.get_page(page)

    except PageNotAnInteger:
        contacts = paginator.page(1)

    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return contacts


def log_out(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER'))


def profile_edit(request):
    if not request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":

        form = RegisterForm(data=request.POST,
                            files=request.FILES,
                            instance=request.user)
        if form.is_valid():

            print("okok")
            nickname = form.clean_nickname()
            password = form.clean_password()
            email = form.clean_email()
            request.user.email = email
            request.user.set_password(password)
            request.user.username = form.clean_login()
            request.user.first_name = nickname
            print(request.FILES)
            for item in request.FILES:
                print(item)

            request.user.save()
            login(request, user=request.user)
            form.save()
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            print(form.errors)
            return render(request, "./question/profile.html", {"form": form})
    else:

        data = {'login': request.user.username, 'email': request.user.email, 'nickname': request.user.first_name}
        form = RegisterForm(data, instance=request.user)
        return render(request, "./question/profile.html", {"form": form})


@login_required
def vote(request):
    data = json.loads(request.body)

    if (request.method == "POST"):
        user = UserProfile.objects.get(user=request.user)
        quest = Article.objects.get(pk=data['qid'])
        if (data['vote'] == "inc"):
            quest.like.add(user)
            data['resp'] = quest.like.count()
        else:
            quest.dislike.add(user)
            data['resp'] = quest.dislike.count()

    else:
        print("no")

    return JsonResponse(data)
