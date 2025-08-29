from django.urls import path
from . import views

urlpatterns = [
    path('api/registration/', views.registration_view, name='registration-api')
]
