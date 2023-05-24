from django.contrib import admin

from .models import Products


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name', 'description')
    list_filter = ('price',)


admin.site.register(Products, ProductsAdmin)
