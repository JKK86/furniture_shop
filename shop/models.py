from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64, db_index=True)
    slug = models.SlugField(max_length=64, unique=True, db_index=True)

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"
        ordering = ('name',)
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['slug']),
        ]

    def __str__(self):
        return self.name


class Wood(models.Model):
    type = models.CharField(max_length=32, verbose_name="Rodzaj")
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Rodzaj drewna"
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
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    wood = models.ForeignKey(Wood, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='products/%Y/%m/%d/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Produkt"
        verbose_name_plural = "Produkty"
        ordering = ('name',)
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['slug']),
        ]

    def __str__(self):
        return self.name
