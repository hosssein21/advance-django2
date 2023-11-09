from django.urls import path
from . import views

app_name='blog'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('cbv/',views.IndexView.as_view(),name='redirect'),
    path('posts/',views.PostList.as_view(),name='posts'),
    path('post/<int:pk>/',views.PostDetail.as_view(),name='post_detail'),
]
