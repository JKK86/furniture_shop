from django.contrib import admin

from coupon.models import Coupon


@admin.register(Coupon)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['code', 'valid_from', 'valid_to', 'active', 'discount']
    list_filter = ['active', 'valid_from', 'valid_to']
    list_editable = ['discount', 'active']
    search_fields = ['code']
