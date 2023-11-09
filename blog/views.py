from typing import Any
from django.shortcuts import render
from .models import Post
from django.views.generic import TemplateView,RedirectView,ListView,DetailView

class IndexView(TemplateView):
    template_name='blog/index.html'
    
    def get_context_data(self, **kwargs: Any):
        context= super().get_context_data(**kwargs)
        context['name']="hosssein"
        return context
    
class RedirectUrl(RedirectView):
    url='https://gist.github.com/robgolding/3092600'
    
class PostList(ListView):
    #model=Post
    queryset=Post.objects.filter(Active=1)
    context_object_name='posts'
    template_name='blog/posts.html'
    
class PostDetail(DetailView):
    queryset=Post.objects.filter(Active=1)
    template_name='blog/post.html'