from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
class storeviews:
    def store(request: HttpRequest):
        return render(request=HttpRequest, template_name='store.html') 