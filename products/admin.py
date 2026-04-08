from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ["name","price","category","is_trending"]

    list_filter = ["category","is_trending"]

    search_fields = ["name"]