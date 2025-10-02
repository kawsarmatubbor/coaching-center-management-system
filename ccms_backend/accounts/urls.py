from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/registration/', views.registration_view, name='registration-api'),
    path('api/login/', TokenObtainPairView.as_view(), name='login-api'),
    path('api/refresh/', TokenRefreshView.as_view(), name='refresh-api'),
    path('api/profile/', views.profile_view, name='profile-api'),
]
