from django.db import models


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
