from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

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


class Category(models.Model):
    name = models.CharField(max_length=64, verbose_name="Nazwa")
    slug = models.SlugField(max_length=64, unique=True)

    class Meta:
        verbose_name = "kategorię"
        verbose_name_plural = "Kategorie"
        ordering = ('name',)
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['slug']),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list_by_category', args=[self.slug])


class Wood(models.Model):
    type = models.CharField(max_length=32, verbose_name="Nazwa")
    description = models.TextField(blank=True, verbose_name="Opis")

    class Meta:
        verbose_name = "rodzaj drewna"
        verbose_name_plural = "Rodzaje drewna"
        ordering = ('type',)

    def __str__(self):
        return self.type


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name="Nazwa")
    slug = models.SlugField(max_length=128)
    description = models.TextField(blank=True, verbose_name="Opis")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Cena")
    stock = models.IntegerField(verbose_name="Dostępność")
    width = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="Szerokość")
    depth = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="Głębokość")
    height = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="Wysokość")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", verbose_name="Kategoria")
    wood = models.ForeignKey(Wood, on_delete=models.CASCADE, verbose_name="Rodzaj drewna")
    image = models.ImageField(blank=True, upload_to='products/%Y/%m/%d/', verbose_name="Zdjęcie")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Data dodania")
    updated = models.DateTimeField(auto_now=True, verbose_name="Data modyfikacji")

    class Meta:
        verbose_name = "produkt"
        verbose_name_plural = "Produkty"
        ordering = ('name',)
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['slug']),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id, self.slug])


class CustomizedProduct(models.Model):
    name = models.CharField(max_length=128, verbose_name="Nazwa")
    slug = models.SlugField(max_length=128, blank=True)
    description = models.TextField(verbose_name="Opis")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="customized_products",
                                 verbose_name="Kategoria")
    wood = models.ForeignKey(Wood, on_delete=models.CASCADE, verbose_name="Rodzaj drewna")
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, verbose_name="Cena")
    file = models.FileField(upload_to="files", blank=True, verbose_name="Plik",
                            help_text="Załącz plik z rysunkiem w formacie jpg lub pdf")
    color = models.CharField(max_length=8, choices=COLORS, default=NATURALNY, verbose_name="Kolor")
    width = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="Szerokość")
    depth = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="Głębokość")
    height = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="Wysokość")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Data dodania")
    updated = models.DateTimeField(auto_now=True, verbose_name="Data modyfikacji")
    status = models.BooleanField(default=False, verbose_name="Status")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Klient")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            super().save(*args, **kwargs)

    class Meta:
        verbose_name = "produkt na zamówienie"
        verbose_name_plural = "Produkty na zamówienie"
        ordering = ('created',)
