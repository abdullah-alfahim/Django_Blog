from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Blog



from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog

class HomeView(ListView):
    model = Blog
    context_object_name = 'blogs'


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    success_url = reverse_lazy('home')
    fields = ['heading', 'keywords', 'image', 'description']
    template_name = 'config/blog_create.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
class ProfileView(LoginRequiredMixin, ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'config/profile.html'
