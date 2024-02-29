from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("home/",views.home,name ="home"),
    path("index/",views.index,name= "index"),
    path("",views.home, name='home'),
    path('select_style/', views.select_style,name= 'select_style'),
    path("search/",views.search, name='search'),
]