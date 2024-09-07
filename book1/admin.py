from django.contrib import admin

from .models import Book, Author


class BookLineAdmin(admin.TabularInline):
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookLineAdmin]
