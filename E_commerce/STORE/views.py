from django.http import HttpRequest
from django.shortcuts import render
from . import views
# Create your views here.
def store(request):
        return render(request,'store.html',name="store") 