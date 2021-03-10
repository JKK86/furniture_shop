from django.contrib import admin

from shop.custom_filters import AvailableFilter
from shop.models import Product, Category, Wood


def dimensions(obj):
    return f"{obj.width} x {obj.depth} x {obj.height} cm"


dimensions.short_description = 'Wymiary'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = ['created', 'updated', ]
    list_display = ['name', 'slug', dimensions, 'price', 'stock', 'category', 'wood', 'created', 'updated', ]
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['updated', 'created', AvailableFilter, 'wood']
    list_editable = ['price', 'stock']
    search_fields = ['name']


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', ]
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Wood)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['type', 'description', ]
