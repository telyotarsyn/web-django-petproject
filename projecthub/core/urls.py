from django.urls import path
from django.shortcuts import render
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
]

def home(request):
    return render(request, "core/home.html")