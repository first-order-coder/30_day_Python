from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView, 
    CreateView
)
from .models import Post

# Create your views here.
def home(request):
    # return HttpResponse('<h1>Blog Home</h1>')
    context = {
        "posts":Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #it will automatically look inside templates folder
    context_object_name = 'posts'
    ordering = ['-date_posted'] #this order the posts from newest to oldest

class PostDetailView(DetailView):
    model = Post 

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

