from decimal import Decimal

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from cart.models import COLORS, NATURALNY
from coupon.models import Coupon
from shop.models import Product

ODBIOR = "OD"
KURIER = "KR"
POCZTA = "PO"
DELIVERY_TYPES = (
    (ODBIOR, 'Odbiór osobisty'),
    (KURIER, 'Dostawa kurierem'),
    (POCZTA, 'Dostawa pocztą')
)


class DeliveryAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Użytkownik")
    address = models.CharField(max_length=255, verbose_name="Adres")
    postal_code = models.CharField(max_length=6, verbose_name="Kod pocztowy")
    city = models.CharField(max_length=64, verbose_name="Miasto")

    def __str__(self):
        return f'{self.address}, {self.postal_code} {self.city}'

    class Meta:
        verbose_name = 'adres dostawy'
        verbose_name_plural = 'Adresy dostawy'
        ordering = ('user',)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Użytkownik")
    products = models.ManyToManyField(Product, through='OrderItem', verbose_name="Produkty")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Data dodania")
    updated = models.DateTimeField(auto_now=True, verbose_name="Data modyfikacji")
    paid = models.BooleanField(default=False, verbose_name="Opłacone")
    delivery = models.CharField(max_length=2, choices=DELIVERY_TYPES, default=ODBIOR, verbose_name="Dostawa")
    delivery_address = models.ForeignKey(DeliveryAddress, on_delete=models.SET_NULL, null=True,
                                         verbose_name="Adres dostawy")
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Kupon")
    discount = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name="Zniżka", default=0)

    def get_total_cost(self):
        total_cost = sum([item.quantity * item.product.price for item in self.orderitem_set.all()])
        return total_cost - total_cost * (self.discount / Decimal('100'))

    def __str__(self):
        return f"Zamówienie nr {self.id}"

    class Meta:
        verbose_name = 'zamówienie'
        verbose_name_plural = 'zamówienia'
        ordering = ('-created',)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Cena")
    color = models.CharField(max_length=8, choices=COLORS, default=NATURALNY)
