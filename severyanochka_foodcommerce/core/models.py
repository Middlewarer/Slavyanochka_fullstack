from django.db import models

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


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    rate = models.DecimalField(max_digits=3, decimal_places=1)
    date = models.DateTimeField(auto_now=True)

