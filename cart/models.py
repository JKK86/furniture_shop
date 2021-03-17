from decimal import Decimal

from django.contrib.auth.models import User
from django.db import models

from coupon.models import Coupon
from shop.models import Product

NATURALNY = 'Natural'
DAB_JASNY = "#935B2A"
DAB_CIEMNY = "#381A10"
MAHON = "#B35D32"
BIEL = 'White'
ORZECH_CIEMNY = '#30180D'
ORZECH_JASNY = '#5F311B'
ZIELEN = '#444213'
ORANZ = '#C37437'
CZARNY = 'Black'

COLORS = (
    (NATURALNY, 'Naturalny'),
    (DAB_JASNY, 'Dąb jasny'),
    (DAB_CIEMNY, 'Dąb ciemny'),
    (MAHON, 'Mahoń'),
    (BIEL, 'Biel'),
    (ORZECH_JASNY, 'Orzech'),
    (ZIELEN, 'Zieleń'),
    (ORANZ, 'Oranż'),
    (CZARNY, 'Czerń'),
)


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartProduct')
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True)

    def get_total_price(self):
        items = self.cartproduct_set.all()
        total_price = 0
        for item in items:
            item.total_price = item.quantity * item.product.price
            total_price += item.total_price
        return total_price

    def get_discount(self):
        if self.coupon:
            return (self.coupon.discount/Decimal('100'))*self.get_total_price()
        return Decimal('0')

    def get_total_price_with_discount(self):
        return self.get_total_price() - self.get_discount()

    def __len__(self):
        return sum(item.quantity for item in self.cartproduct_set.all())


class CartProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    color = models.CharField(max_length=8, choices=COLORS, default=NATURALNY)
