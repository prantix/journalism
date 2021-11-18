from django.urls import path
from . import views

app_name = 'journal'

urlpatterns = [
    path('index', views.index, name='index'),
    path('<str:category>/<slug:slug>', views.article_detail, name='detail'),
]