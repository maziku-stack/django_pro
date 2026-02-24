from django.urls import path

from E_commerce.STORE import views


urlpatterns = [
    path('', views.store, name='store')

]