from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.OrderView.as_view(), name='orders'),
    path('', views.CartView.as_view(), name='cart'),
    path('offer/', views.OfferOrderView.as_view(), name='cart'),
]