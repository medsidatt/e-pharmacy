from django.urls import path

from webapp.home.views import home

urlpatterns = [
    path('', home, name='index'),
]