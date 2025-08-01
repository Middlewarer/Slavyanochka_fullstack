from django.db import models
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey('core.Product', on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=1)

class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'В ожидании'
        PAID = 'PAID', 'Оплачен'
        SHIPPED = 'SHIPPED', 'Отправлен'
        DELIVERED = 'DELIVERED', 'Доставлен'
        CANCELED = 'CANCELED', 'Отменён'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('core.Product', on_delete=models.PROTECT)
    quantity = models.SmallIntegerField()
    price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)
