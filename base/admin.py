import imp
from pickletools import read_uint1
from django.contrib import admin
from .models import Quizz,QuizzAnswer,QuizzQuestion,Results

# Register your models here.
admin.site.register(Quizz)
admin.site.register(QuizzAnswer)
admin.site.register(QuizzQuestion)
admin.site.register(Results)