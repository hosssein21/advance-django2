from django.urls import path,include
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


app_name='api-v1'

urlpatterns = [
    path('registration/',views.RegistrationApiView.as_view(),name='registration'),
    path('token/login/',views.CustomObtainAuthToken.as_view(),name='token-login'),
    path('token/logout/',views.CustomDiscardToken.as_view(),name='token-logout'),
    
    #JWT token
    
    path('jwt/create/', TokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('jwt/token/verify/', TokenVerifyView.as_view(), name='jwt-verify'),
    
    path('change-password/',views.change_password,name='change-password'),
    path('profile/',views.ProfileApiView.as_view(),name='profile'),
    
]
