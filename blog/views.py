from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm


#def blog(request):
#   return render(request, 'blog/blog.html', {})

class BlogView(ListView):
    model = Post
    template_name = 'blog/blog.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_details.html'


class AddBlogView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_blog.html'
    #fields = ('title', 'intro', 'body')
