from django.shortcuts import render

from django.urls import reverse_lazy 
from .forms import PostForm 
from .models import Post 

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView 
from .models import Post

class PostListView(ListView):
    model = Post #nombre de la tabla
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    #queryset = Post.objects.filter(published=True).order_by('-created_at')
    queryset = Post.objects.all().order_by('-created_at')

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class PostCreateView(CreateView): 
    model = Post 
    form_class = PostForm 
    template_name = 'blog/post_form.html' 
    success_url = reverse_lazy('post_list')  # redirección tras crear 

    
class PostUpdateView(UpdateView): 
    model = Post 
    form_class = PostForm 
    template_name = 'blog/post_form.html' 
    success_url = reverse_lazy('post_list')