from django.utils import timezone
from datetime import timedelta

from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from .models import Product


class MainPageView(TemplateView):
    template_name = 'core/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['specials'] = Product.objects.filter(discount__gte=1)

        today = timezone.now().date()
        context['new_ones'] = Product.objects.filter(created_at__date=today)
        return context

    def post(self, request):
        query = request.POST.get('q', '')
        return redirect(f"/search/?q={query}")


class SearchPageView(ListView):
    model = Product
    template_name = 'core/search_page.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = Product.objects.filter(title__icontains=self.request.GET.get('q'))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context
