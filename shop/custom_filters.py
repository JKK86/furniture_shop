from django.contrib.admin import SimpleListFilter


class AvailableFilter(SimpleListFilter):
    """Filter that is used in admin panel in product model"""

    title = "Dostępny"
    parameter_name = "available"

    def lookups(self, request, model_admin):
        return (
            ('available', 'Dostępny'),
            ('not_available', 'Niedostępny'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'available':
            return queryset.filter(stock__gt=0)
        if self.value() == 'not_available':
            return queryset.filter(stock=0)
