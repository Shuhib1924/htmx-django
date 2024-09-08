from django.contrib import admin
from .models import Country, City


class CityLineAdmin(admin.TabularInline):
    model = City


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    inlines = [CityLineAdmin]
