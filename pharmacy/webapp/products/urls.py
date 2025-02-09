from django.urls import path

from webapp.products import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create_product, name='create'),
]