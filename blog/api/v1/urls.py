from django.urls import path
from . import views

urlpatterns =[
    path('index/',views.api_index),
    path('post/<int:pk>/',views.PostDetailGeneric.as_view()),
    path('posts/',views.PostListGeneric.as_view()),
]