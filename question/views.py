from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from question import models


# Create your views here.

def one_question(request, name):
    try:
        title=models.Article.objects.get(pk=name).title
    except models.Article.DoesNotExist:
        return render(request, "./question/404.html")

    answers = models.Answer.objects.by_question(name)
    paginated_data = paginate(answers, request)
    rendered_data = {"questions": paginated_data, "title": title}
    return render(request, "./question/one_question.html", rendered_data)


def index_html(request):
    # return HttpResponse(year, content_type="text/plain")

    articles = models.Article.objects.new_published()
    paginated_data = paginate(articles, request)
    rendered_data = {"questions": paginated_data}

    return render(request, "./question/index.html", rendered_data)


def login_html(request):
    return render(request, "./question/login.html")


def register_html(request):
    return render(request, "./question/register.html")


def add_question_html(request):
    return render(request, "./question/add_question.html")


def questions_by_tag_html(request, tag="kek"):
    data_list = list()
    for i in range(1, 10):
        data_list.append({"name": tag + " " + str(i)})  # заглушка
    data = {
        "questions": data_list}

    paginated_data = paginate(data["questions"], request)

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
