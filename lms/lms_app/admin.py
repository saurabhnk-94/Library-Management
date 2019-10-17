from django.contrib import admin
from lms_app.models import *
from django import forms
import re


class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name','address','city','email','membership_fee')
    ordering = ('name',)
    search_fields = ['name','city']


admin.site.register(Library, LibraryAdmin)


class LibrarianAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LibrarianAdminForm, self).__init__(*args, **kwargs)

    def clean(self):
        contact = self.cleaned_data.get('contact_number')
        if contact is not None:
            regex = r'^\d{10}$'
            match = re.match(regex, contact)
            if match is None:
                raise forms.ValidationError("Contact Number should be 10 digits",code='invalid')
        return self.cleaned_data

    def save(self, commit=True):
        return super(LibrarianAdminForm, self).save(commit=commit)


class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('full_name','library','contact_number')
    list_filter = ('library',)
    ordering = ('first_name',)
    search_fields = ['first_name','middle_name','last_name',]
    form = LibrarianAdminForm


admin.site.register(Librarian, LibrarianAdmin)


class BookAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookAdminForm, self).__init__(*args, **kwargs)

    def clean(self):
        isbn = self.cleaned_data.get('isbn')
        total_stock = self.cleaned_data.get('total_stock')
        available_stock = self.cleaned_data.get('available_stock')
        if total_stock != available_stock:
            raise forms.ValidationError("Total stock and Available stock must be equal.")
        if isbn is not None:
            regex = r'^(\d{3})(\s|\-)(\d{1,5})(\s|\-)(\d{1,7})(\s|\-)(\d{1,6})(\s|\-)(\d{1})$'
            match = re.match(regex, isbn)
            if match is None:
                raise forms.ValidationError("ISBN Code: x{3}-x{1,5}-x{1-7}-x{1-6}-x{1} where x is the number {length of the digits}")
        return self.cleaned_data

    def save(self, commit=True):
        return super(BookAdminForm, self).save(commit=commit)


class BookAdmin(admin.ModelAdmin):
    list_display = ('name_of_the_book','publication','isbn','author','library','available','price','total_stock','available_stock')
    list_filter = ('available','library')
    search_fields = ['name_of_the_book','publication','author']
    ordering = ('name_of_the_book',)
    form = BookAdminForm


admin.site.register(Book, BookAdmin)

class MemberAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MemberAdminForm, self).__init__(*args, **kwargs)

    def clean(self):
        contact = self.cleaned_data.get('contact_number')
        if contact is not None:
            regex = r'^\d{10}$'
            match = re.match(regex, contact)
            if match is None:
                raise forms.ValidationError("Contact Number should be 10 digits",code='invalid')
        return self.cleaned_data

    def save(self, commit=True):
        return super(MemberAdminForm, self).save(commit=commit)

class MemberAdmin(admin.ModelAdmin):
    list_display = ('full_name','contact_number','address','membership','book_count')
    ordering = ('first_name',)
    search_fields = ['first_name','middle_name','last_name']
    list_filter = ('membership',)
    form = MemberAdminForm


admin.site.register(Member, MemberAdmin)


class RecordAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RecordAdminForm, self).__init__(*args, **kwargs)
        if not self.instance.id:
            self.fields['returned'].disabled = True
            self.fields['date_returned'].disabled = True

        else:
            l =['member','book','issue_date','date_of_return','librarian_name']
            for i in l:
                self.fields[i].disabled = True


    def clean(self):
        book = self.cleaned_data.get('book')
        if self.cleaned_data.get('returned') == False:
            if self.cleaned_data.get('date_returned') is None:
                if book.available == False:
                    raise forms.ValidationError("Stock is not available",code='invalid')
            else:
                raise forms.ValidationError("Please check the returned field while returning",code='invalid')
        else:
            if self.cleaned_data.get('date_returned') is None:
                raise forms.ValidationError("Please enter the date returned field",code='invalid')
        return self.cleaned_data

    def save(self, commit=True):
        return super(RecordAdminForm, self).save(commit=commit)


class RecordAdmin(admin.ModelAdmin):
    list_display =('id','member','book','issue_date','penalty_per_day','date_of_return','date_returned','librarian_name','total_fine')
    ordering = ('member',)
    list_filter = ('librarian_name__library',)
    search_fields = ['member','book']
    form = RecordAdminForm


admin.site.register(Record, RecordAdmin)