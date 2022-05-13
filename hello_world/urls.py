from turtle import home
from django.urls import URLPattern, path
from django.views import View
from . import views

urlpatterns=[
    path("",views.homepage,name="home"),
    path("sayhello",views.say_hello,name="hello")
    ]