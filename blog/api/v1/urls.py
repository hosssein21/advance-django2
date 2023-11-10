from django.urls import path
from . import views

urlpatterns =[
    path('index/',views.api_index),
    path('post/<int:pk>/',views.post_detail),
    path('posts/',views.all_post),
]