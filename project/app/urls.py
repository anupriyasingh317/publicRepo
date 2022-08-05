from django.contrib import admin
from django.urls import path, include

from . import views
urlpatterns = [

     path('', views.basic,name='basic'),
    path('repository/', views.Repo, name="repository"),

]