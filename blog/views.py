from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #Used to display template using class based views
    context_object_name = 'posts'
    ordering = ['-date_posted'] #To display most recent posts at top/inverse order

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
