from django.test import TestCase,SimpleTestCase
from django.urls import reverse,resolve
from ..views import IndexView, PostDetail, PostList

class TestUrl(SimpleTestCase):
    
    def test_blog_index_url_resolve(self):
        url=reverse('blog:index')
        self.assertEquals(resolve(url).func.view_class, IndexView)
        
    def test_blog_post_list_url_resolve(self):
        url=reverse('blog:posts')
        self.assertEquals(resolve(url).func.view_class,PostList)
        
    def test_blog_post_detail_url_resolve(self):
        url=reverse('blog:post_detail',kwargs={'pk':1})
        self.assertEquals(resolve(url).func.view_class,PostDetail)