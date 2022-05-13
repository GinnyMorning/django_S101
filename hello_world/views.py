from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request,'index.html',context={})

def say_hello(request):
    return HttpResponse('Hello world')