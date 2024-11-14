from django.contrib import admin

from .models import Book, Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("description", "value", "paid")
    list_filter = ("paid",)
    search_fields = ("description",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
    search_fields = ("title", "author")
