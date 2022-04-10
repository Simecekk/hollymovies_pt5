from django.contrib import admin
from books.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'number_of_pages']


admin.site.register(Book, BookAdmin)
