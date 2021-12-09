from django.views.generic import ListView, DetailView
from .models import Post, Category

class PostList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'new'
