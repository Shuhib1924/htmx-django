from django.contrib import admin

from .models import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("description", "value", "paid")
    list_filter = ("paid",)
    search_fields = ("description",)
