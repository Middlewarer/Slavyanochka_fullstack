from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPageView.as_view(), name='main'),
    path('search/', views.SearchPageView.as_view(), name='search')
]