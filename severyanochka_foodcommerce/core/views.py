from unicodedata import category

from django.utils import timezone
from datetime import timedelta

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView
from .models import Product, Category


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


class SearchByCatalogPageView(ListView):
    model = Product
    template_name = 'core/search_catalog.html'
    context_object_name = 'products'

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Product.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context


class CatalogPageView(TemplateView):
    template_name = 'core/categorys.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorys'] = Category.objects.all()
        return context
