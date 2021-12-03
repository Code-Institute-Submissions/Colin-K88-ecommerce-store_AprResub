#from . import views
from django.urls import path
from.views import BlogView, BlogDetailView, AddBlogView

urlpatterns = [
    #path('', views.blog, name='blog'),
    path('', BlogView.as_view(), name='blog'),
    path('article/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('add_blog/', AddBlogView.as_view(), name='add_blog'),
]
