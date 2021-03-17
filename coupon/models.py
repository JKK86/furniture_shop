from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Coupon(models.Model):
    code = models.CharField(max_length=16, unique=True, verbose_name="Kod")
    valid_from = models.DateTimeField(verbose_name="Ważny od")
    valid_to = models.DateTimeField(verbose_name="Ważny do")
    active = models.BooleanField(verbose_name="Aktywny")
    discount = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name="Zniżka")

    class Meta:
        verbose_name = "kupon"
        verbose_name_plural = "Kupony"
        ordering = ('-active', '-valid_to')

    def __str__(self):
        return self.code
