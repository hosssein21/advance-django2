from django.shortcuts import render
from .models import Post
from django.views.generic import (TemplateView,RedirectView,ListView,DetailView ,\
                                    CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin

class IndexView(TemplateView):
    template_name='blog/index.html'
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['name']="hosssein"
        return context
    
class RedirectUrl(RedirectView):
    url='https://gist.github.com/robgolding/3092600'
    
class PostList(ListView):
    #model=Post
    queryset=Post.objects.all()
    context_object_name='posts'
    template_name='blog/posts.html'
    
class PostDetail(PermissionRequiredMixin,LoginRequiredMixin,DetailView):
    permission_required='blog.view_post_detail'
    queryset=Post.objects.filter(Active=1)
    template_name='blog/post.html'
    
class PostCreate(CreateView):
    template_name="blog/create.html"
    model=Post
    fields=["title","content","author","category"]
    success_url="/blog/posts/"
    
class PostUpdate(UpdateView):
    template_name="blog/create.html"
    model=Post
    fields=["title","content"]
    success_url="/blog/posts/"
    
class PostDelete(DeleteView):
    template_name='blog/delete.html'
    model=Post
    success_url="/blog/posts/"