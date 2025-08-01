from unicodedata import category

from django.utils import timezone
from datetime import timedelta

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from .models import Product, Category
from django.db.models import Q


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
    template_name = 'core/search_by_catalog.html'
    context_object_name = 'products'

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        queryset = Product.objects.filter(category=self.category)
        in_stock = self.request.GET.get('in_stock')
        f_from = self.request.GET.get('from')
        f_to = self.request.GET.get('to')

        if in_stock:
            queryset = queryset.filter(count__gte=1)

        if f_from:
            queryset = queryset.filter(price__gte=f_from)

        if f_to:
            queryset = queryset.filter(price__lte=f_to)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['in_stock'] = self.request.GET.get('in_stock')
        context['f_from'] = self.request.GET.get('from')
        context['f_to'] = self.request.GET.get('to')
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'core/product_detail.html'



class CatalogPageView(TemplateView):
    template_name = 'core/categorys.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorys'] = Category.objects.all()
        return context


class SpecialPageView(ListView):
    template_name = 'core/special.html'
    model = Product


    def get_queryset(self):
        queryset = Product.objects.all()
        in_stock = self.request.GET.get('in_stock')
        f_from = self.request.GET.get('from')
        f_to = self.request.GET.get('to')

        if in_stock:
            queryset = queryset.filter(count__gte=1)

        if f_from:
            queryset = queryset.filter(price__gte=f_from)

        if f_to:
            queryset = queryset.filter(price__lte=f_to)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['in_stock'] = self.request.GET.get('in_stock')
        context['f_from'] = self.request.GET.get('from')
        context['f_to'] = self.request.GET.get('to')
        return context
