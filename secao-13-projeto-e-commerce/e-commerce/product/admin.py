from django.contrib import admin
from .models import Product, Variation


class VariationInLine(admin.TabularInline):
    model = Variation
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [VariationInLine]


admin.site.register(Product, ProductAdmin)
admin.site.register(Variation)