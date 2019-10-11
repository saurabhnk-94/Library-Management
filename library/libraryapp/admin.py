from django.contrib import admin

# Register your models here.

from .models import Book, Author


class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name','book_price','availability','upper_name','isbn','author_name')
    list_filter = ('availability',)
    search_fields = ['book_name','book_price']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_fname','author_lname','full_name')

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)

