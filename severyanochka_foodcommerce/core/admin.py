from django.contrib import admin
from .models import Product, ProductImages, Category

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductImages)
admin.site.register(Category)