from django.contrib import admin

# Register your models here.

from .models import Book,Author,Member


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_name','author_mail')
    search_fields = ['author_name']


class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name','availability','isbn','author_obj__author_name')
    list_filter = ('availability',)
    search_fields = ['book_name']


class MemberAdmin(admin.ModelAdmin):
    list_display = ('member_id','member_name','contact')

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register()

