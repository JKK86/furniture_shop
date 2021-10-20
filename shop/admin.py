from django.contrib import admin
from django.contrib.auth.models import User
from django.core.mail import send_mail

from shop.custom_filters import AvailableFilter
from shop.models import Product, Category, Wood, CustomizedProduct, OFFER


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
    list_editable = ['price', 'status', 'date']
    search_fields = ['name']
    actions = ['send_offer']

    def send_offer(self, request, queryset):
        queryset.update(status=OFFER)
        for obj in queryset:
            subject = f"Oferta na wykonanie projektu na zamowienie"
            subject = subject[0][0]
            message = f"""Witaj, {obj.user.first_name}, 
przeanalizowaliśmy Twoje zlecenie na wykonanie {obj.name}.
Poniżej proponowana cena wykonania projektu oraz termin realizacji:
Cena: {obj.price},
Przewidywana data realizacji: {obj.date}            
Prosimy o potwierdzenie zamówienia w ciągu najbliższych 3 dni roboczych,
Sklep Meblowy
            """
            email_from = "furniture_shop@local.com"
            admins = User.objects.filter(is_staff=True)
            email_to = [obj.user.email]
            send_mail(subject, message, email_from, email_to, fail_silently=False)

    send_offer.short_description = "Wyślij oferty"