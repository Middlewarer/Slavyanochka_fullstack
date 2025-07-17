from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegistrationPageView.as_view(), name='register_page'),
    path('index/', views.index, name='index')
]