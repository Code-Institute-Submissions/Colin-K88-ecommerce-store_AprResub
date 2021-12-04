#from . import views
from django.urls import path
from.views import BlogView, BlogDetailView, AddBlogView, UpdateBlogView, DeleteBlogView

urlpatterns = [
    #path('', views.blog, name='blog'),
    path('', BlogView.as_view(), name='blog'),
    path('article/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('add_blog/', AddBlogView.as_view(), name='add_blog'),
    path('article/edit/<int:pk>', UpdateBlogView.as_view(), name='update_blog'),
    path('article/<int:pk>/delete', DeleteBlogView.as_view(), name='delete_blog'),
]
