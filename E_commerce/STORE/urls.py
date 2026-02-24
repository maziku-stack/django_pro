from django.urls import path
from .views import storeviews


urlpatterns = [
    path('', storeviews.store, name='store')

]