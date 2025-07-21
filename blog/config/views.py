from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Blog
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

class UpdateView(UpdateView):
    model = Blog
    success_url = reverse_lazy('profile')
    fields = ['heading', 'keywords', 'image', 'description']
    template_name = 'config/blog_create.html'


class DeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('profile')
    template_name = 'config/blog_delete.html'

