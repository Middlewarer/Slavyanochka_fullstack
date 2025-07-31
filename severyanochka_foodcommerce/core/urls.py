from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPageView.as_view(), name='main'),
    path('search/', views.SearchPageView.as_view(), name='search'),
    path('products/<slug:slug>/', views.SearchByCatalogPageView.as_view(), name='catalog_search'),
    path('catalog/', views.CatalogPageView.as_view(), name='catalog'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='detail'),
]