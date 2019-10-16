from django.contrib import admin
from django import forms
# Register your models here.

from .models import *


class AuthorAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AuthorAdminForm, self).__init__(*args, **kwargs)

    def clean(self):
        author_name = self.cleaned_data.get('author_name')
        if len(author_name) < 4:
            raise forms.ValidationError('Author name should not be less that 4 characters',code='invalid')
        return self.cleaned_data

    def save(self, commit=True):
        return super(AuthorAdminForm, self).save(commit=commit)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_name','author_mail')
    ordering = ('author_name',)
    search_fields = ['author_name']
    form = AuthorAdminForm


class BookAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookAdminForm, self).__init__(*args, **kwargs)

    def clean(self):
        isbn = self.cleaned_data.get('isbn')
        if len(isbn) < 10:
            raise forms.ValidationError('ISBN is not Valid, should be more that 10 chararcters',code='invalid')

        return self.cleaned_data

    def save(self, commit=True):
        return super(BookAdminForm, self).save(commit=commit)


class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name','availability','isbn','author_name','total_books','stock')
    ordering = ('book_name',)
    list_filter = ('availability',)
    search_fields = ['book_name']
    form = BookAdminForm


class MemberAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MemberAdminForm, self).__init__(*args, **kwargs)

    def clean(self):
        contact = self.cleaned_data.get('contact')
        if len(str(contact)) != 10:
            raise forms.ValidationError("Please Enter the Valid Phone Number which is Of 10 digits", code='invalid')
        return self.cleaned_data

    def save(self, commit=True):
        return super(MemberAdminForm, self).save(commit=commit)


class MemberAdmin(admin.ModelAdmin):
    list_display = ('member_name','contact','member_mail','member_address')
    ordering = ('member_name',)
    search_fields = ['member_name']
    form = MemberAdminForm


class RecordAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RecordAdminForm, self).__init__(*args, **kwargs)

    def clean(self):
        book = self.cleaned_data.get('book')
        if book.stock == 0:
            if self.cleaned_data.get('returned') == False:
                raise forms.ValidationError('Book is out of stock',code='invalid')
        return self.cleaned_data

    def save(self, commit=True):
        return super(RecordAdminForm, self).save(commit=commit)


class RecordAdmin(admin.ModelAdmin):
    list_display = ('book','issue_date','return_date', 'member_name','returned',)
    ordering = ('book',)
    search_fields = ['book__book_name',]
    form = RecordAdminForm


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Record, RecordAdmin)
