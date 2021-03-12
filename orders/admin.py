from django.contrib import admin

from orders.models import OrderItem, Order, DeliveryAddress


class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdminInline,)


admin.site.register(Order, OrderAdmin)


@admin.register(DeliveryAddress)
class DeliveryAddressAdminInline(admin.ModelAdmin):
    list_display = ['user', 'address', 'postal_code', 'city']
