from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect

from question import models
from question.forms import LoginForm, RegisterForm
from userprofile.models import UserProfile


def one_question(request, m_id):
    try:
        main_quest = models.Article.objects.get(pk=m_id)
    except (models.Article.DoesNotExist, ValueError):
        return render(request, "./question/404.html")
    answers = models.Answer.objects.by_question(m_id)
    paginated_data = paginate(answers, request)
    rendered_data = {"questions": paginated_data, "main_question": main_quest}
    return render(request, "./question/one_question.html", rendered_data)


def index_html(request):
    articles = models.Article.objects.new_published()
    paginated_data = paginate(articles, request)
    rendered_data = {"questions": paginated_data}
    return render(request, "./question/index.html", rendered_data)


def login_html(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            print("OK")
            username = form.clean_username()
            password = form.clean_password()
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
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
        print(request.POST)
        form = RegisterForm(request.POST)

        if not form.is_valid():
            print("OK")
            username = form.clean_login()
            password = form.clean_password()
            email = form.clean_email()
            nickname = form.clean_nickname()
            avatar = form.clean_avatar()
            user = User.objects.create_user(username=username, password=password, email=email)
            user.first_name = nickname
            user.avatar = avatar
            user.save()
            return redirect('/')
        else:
            print(form.errors)
            return render(request, "./question/register.html", {"form": form})
    else:
        form = RegisterForm()
        return render(request, "./question/register.html", {"form": form})


def add_question_html(request):
    return render(request, "./question/add_question.html")


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
    paginator = Paginator(objects_list, 3)

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
