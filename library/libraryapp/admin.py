from django.contrib import admin

# Register your models here.

from .models import *


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_name','author_mail')
    ordering = ('author_name',)
    search_fields = ['author_name']


class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name','availability','isbn','author_name','total_books','stock')
    ordering = ('book_name',)
    list_filter = ('availability',)
    search_fields = ['book_name']


class MemberAdmin(admin.ModelAdmin):
    list_display = ('member_id','member_name','contact','member_mail')
    ordering = ('member_name',)
    search_fields = ['member_name']


class RecordAdmin(admin.ModelAdmin):
    list_display = ('book','issue_date','return_date', 'member_name','returned',)
    ordering = ('book',)
    search_fields = ['book__book_name',]


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Record, RecordAdmin)
