from django.db import models
from datetime import datetime, timedelta, date
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save

class Library(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    membership_fee = models.FloatField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Library'
        verbose_name_plural = 'Libraries'


class Librarian(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=10, null=True, blank=True)

    def full_name(self):
        if self.middle_name is None:
            return self.first_name + ' ' + self.last_name
        else:
            return "{} {} {}".format(self.first_name, self.middle_name, self.last_name)

    def __str__(self):
        return self.full_name()


# class Author(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(null=True, blank=True)
#     contact = models.IntegerField(null=True, blank=True)
#
#     def __str__(self):
#         return self.name
#

class Book(models.Model):
    name_of_the_book = models.CharField(max_length=100)
    publication = models.CharField(max_length=100)
    price = models.FloatField()
    isbn = models.CharField(max_length=50)
    total_stock = models.IntegerField(default=1)
    available_stock = models.IntegerField(default=1)
    available = models.BooleanField(default=True)
    author = models.CharField(max_length=50, null=True, blank=True)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_of_the_book


class Member(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50)
    membership = models.ForeignKey(Library, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    book_count = models.IntegerField(null=True)


    def full_name(self):
        if self.middle_name is None:
            return self.first_name + ' ' + self.last_name
        else:
            return "{} {} {}".format(self.first_name, self.middle_name, self.last_name)

    def __str__(self):
        return self.full_name()


class Record(models.Model):
    id = models.AutoField(primary_key=True)
    librarian_name = models.ForeignKey(Librarian, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField(default=date.today())
    date_of_return = models.DateField(default= date.today() + timedelta(days=7))
    date_returned = models.DateField(null=True, blank=True)
    returned = models.BooleanField(default=False)
    penalty_per_day = models.FloatField(default=0)

    def __str__(self):
        return self.book.name_of_the_book

    def total_fine(self):
        if self.date_returned is not None:
            delta = self.date_returned - self.date_of_return
            difference_days = delta.days
            if difference_days > 0:
                return self.penalty_per_day * difference_days
            else:
                return "No fine"


@receiver(post_save,sender=Record)
def decrement_stock(sender,instance,created,**kwargs):
    book = instance.book
    if created:
        if book.available == True:
            book.available_stock = book.available_stock - 1
            if book.available_stock == 0:
                book.available = False
        book.save()
    else:
        if not instance.returned:
            if any(Record.objects.filter(id=instance.id)):
                if Record.objects.get(id=instance.id).returned == True:
                    instance.returned = True
        else:
            book = instance.book
            book.available_stock = book.available_stock + 1
            if book.available_stock > 0:
                book.available = True
            book.save()

# @receiver(pre_save,sender=Record)
# def increment_stock(sender,instance,**kwargs):
#     if not instance.returned:
#         if any(Record.objects.filter(id=instance.id)):
#             if Record.objects.get(id=instance.id).returned == True:
#                 instance.returned = True
#     else:
#         if Record.objects.get(id=instance.id).returned == False:
#             book = instance.book
#             book.available_stock = book.available_stock + 1
#             if book.available_stock > 0:
#                 book.available = True
#             book.save()


@receiver(post_save, sender=Record)
def decrement_total_books(sender,instance,created,**kwargs):
    member = instance.member
    if 0< member.book_count <=4:
        if created:
            if member.book_count > 0:
                member.book_count -= 1
            member.save()

    elif instance.returned == True:
        member.book_count += 1
        member.save()


# @receiver(pre_save,sender=Record)
# def increment_total_books(sender,instance,**kwargs):
#     if not instance.returned:
#         if any(Record.objects.filter(id=instance.id)):
#             if Record.objects.get(id=instance.id).returned == True:
#                 instance.returned = True
#     else:
#         if Record.objects.get(id=instance.id).returned == False:
#             member = instance.member
#             member.book_count += 1
#             member.save()
#
#
#











