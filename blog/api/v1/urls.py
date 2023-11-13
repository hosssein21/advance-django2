from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name='api-v1'

router=DefaultRouter()

router.register('post',views.PostModelViewSet,basename='post')
router.register('category',views.CategoryModelViewSet,basename='category')

urlpatterns =router.urls

# urlpatterns =[
#     path('index/',views.api_index),
#     path('post/<int:pk>/',views.PostViewSet.as_view({'get': 'retrieve'})),
#     path('posts/',views.PostViewSet.as_view({'get':'list'})),
# ]