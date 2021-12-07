from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

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


class UpdateBlogView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/update_blog.html'
    #fields = ('title', 'intro', 'body')


class DeleteBlogView(DeleteView):
    model = Post
    template_name = 'blog/delete_blog.html'
    success_url = reverse_lazy('blog')
