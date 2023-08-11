from django.contrib import admin
from .models import Country, Brand, Phone
# Register your models here.

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "code") 

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "country")

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "brand", "exist", "price")