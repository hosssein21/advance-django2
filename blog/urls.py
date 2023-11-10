from django.urls import path,include
from . import views

app_name='blog'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('cbv/',views.IndexView.as_view(),name='redirect'),
    path('posts/',views.PostList.as_view(),name='posts'),
    path('post/<int:pk>/',views.PostDetail.as_view(),name='post_detail'),
    path('post/create/',views.PostCreate.as_view(),name='post_create'),
    path('post/update/<int:pk>/',views.PostUpdate.as_view(),name='post_update'),
    path('post/delete/<int:pk>/',views.PostDelete.as_view(),name='post_delete'),
    path('api/v1/',include('blog.api.v1.urls'),name='api')
]
