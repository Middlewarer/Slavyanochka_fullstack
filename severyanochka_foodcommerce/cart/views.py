from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import OrderItem, Order


class OrderView(ListView):
    template_name = 'cart/orders.html'
    model = OrderItem
    context_object_name = 'specials'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['orders'] = Order.objects.all()
        return context


class CartView(TemplateView):
    template_name = 'cart/cart_page.html'


class OfferOrderView(TemplateView):
    template_name = 'cart/order_offer.html'


