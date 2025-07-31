from django.db import models
from django.shortcuts import reverse

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('catalog_search', kwargs={'slug': self.slug})


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    brand = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    entity = models.IntegerField()
    discount = models.SmallIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    main_image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    count = models.IntegerField(default=1)


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    rate = models.DecimalField(max_digits=3, decimal_places=1)
    date = models.DateTimeField(auto_now=True)



