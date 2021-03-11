from django.contrib.auth.models import User
from django.db import models

from shop.models import Product


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartProduct')

    def get_total_price(self):
        items = self.cartproduct_set.all()
        total_price = 0
        for item in items:
            item.total_price = item.quantity * item.product.price
            total_price += item.total_price
        return total_price

    def __len__(self):
        return sum(item.quantity for item in self.cartproduct_set.all())


class CartProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
