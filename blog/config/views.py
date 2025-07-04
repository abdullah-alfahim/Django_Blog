from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Blog

# Create your views here.


class HomeView(ListView):
    model = Blog
    context_object_name = 'blogs'




from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin # Import LoginRequiredMixin
from .models import Blog # Assuming Blog model is in config/models.py

class BlogCreateView(LoginRequiredMixin, CreateView): # Add LoginRequiredMixin here
    model = Blog
    success_url = reverse_lazy('home')  # Use reverse_lazy for better practice, assuming 'home' is your home page URL name
    fields = ['heading', 'keywords', 'image', 'description']  # Specify the fields you want in the form
    template_name = 'config/blog_create.html'

    def form_valid(self, form):
        
        form.instance.owner = self.request.user
        
        # Call the parent class's form_valid method to save the object
        # This will save the form.instance (now with owner assigned) to the database
        return super().form_valid(form)
    



