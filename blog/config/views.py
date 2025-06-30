from django.shortcuts import render
from django.views.generic import ListView
from .models import Blog

# Create your views here.


class HomeView(ListView):
    model = Blog
