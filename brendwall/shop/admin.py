from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['title', 'description', 'price']
    list_filter = ['title', 'price']
    search_fields = ['title', 'description', 'price']
    ordering = ['title', 'price']
