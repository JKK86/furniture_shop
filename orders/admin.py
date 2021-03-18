from django.contrib import admin

from orders.models import OrderItem, Order, DeliveryAddress


class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdminInline,)
    list_display = ['id', 'user', 'created', 'updated', 'paid', 'delivery', 'delivery_address', 'coupon', 'discount', ]
    list_filter = ['updated', 'created', 'paid', 'delivery']


admin.site.register(Order, OrderAdmin)


@admin.register(DeliveryAddress)
class DeliveryAddressAdminInline(admin.ModelAdmin):
    list_display = ['user', 'address', 'postal_code', 'city']
