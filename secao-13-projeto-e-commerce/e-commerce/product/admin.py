from django.contrib import admin
from .models import Product, Variation


class VariationInLine(admin.TabularInline):
    model = Variation
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description_short",
        "get_formated_price",
        "get_formated_promotional_price",
    )
    inlines = [VariationInLine]


admin.site.register(Product, ProductAdmin)
admin.site.register(Variation)
