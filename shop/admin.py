from django.contrib import admin

from shop.custom_filters import AvailableFilter
from shop.models import Product, Category, Wood, CustomizedProduct


def dimensions(obj):
    return f"{obj.width} x {obj.depth} x {obj.height} cm"


dimensions.short_description = 'Wymiary'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = ['created', 'updated', ]
    list_display = ['name', 'slug', dimensions, 'price', 'stock', 'category', 'wood', 'created', 'updated', ]
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['updated', 'created', AvailableFilter, 'wood', 'category']
    list_editable = ['price', 'stock']
    search_fields = ['name']


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', ]
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Wood)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['type', 'description', ]


@admin.register(CustomizedProduct)
class CustomizedProductAdmin(admin.ModelAdmin):
    exclude = ['created', 'updated', ]
    list_display = \
        ['name', 'slug', 'category', 'wood', 'price', 'color', dimensions, 'user', 'date', 'status', 'created', 'updated', ]
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['updated', 'created', 'wood', 'category', 'user', 'date']
    list_editable = ['price', 'status']
    search_fields = ['name']
