from . import views
from django.urls import path
from django.urls import include


urlpatterns = [
    path('', views.index, name='index'),
]

