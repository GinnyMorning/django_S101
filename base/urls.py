from multiprocessing import context
from xml.etree.ElementInclude import include
from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('helloworld/', views.hello, name="home"),
]
