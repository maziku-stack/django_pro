from django.http import HttpRequest
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from . import views
# Create your views here.
def store(request):
        try:
            # Simulating an attempt to retrieve an object that might not exist
            # In a real app, this would be replaced with actual logic to retrieve data
             render(request,'store.html') 
        except ObjectDoesNotExist:
            # Handle the case where the object does not exist
             render(request, 'store.html', {'error': 'Object does not exist'})
        