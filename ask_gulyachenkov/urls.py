"""ask_gulyachenkov URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from question import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('question/', views.index_html, name="test"),
    path('question/<str:m_id>', views.one_question, name="one_question_url"),
    path('', views.index_html, name="index"),
    path('login/',views.login_html,name="login_url"),
    path('register/',views.register_html,name="register_url"),
    path('add_question/',views.add_question_html,name="add_question_url"),
    path('question_by_tag/<str:tag>',views.questions_by_tag_html,name="question_by_tag_url"),
    path('hot_questions/',views.hot_questions_html,name="hot_questions_url"),

]
