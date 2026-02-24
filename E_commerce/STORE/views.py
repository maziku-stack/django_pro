
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from . import views
from django.http import  HttpResponse
# Create your views here.
def store(request):
        return HttpResponse("hello world")