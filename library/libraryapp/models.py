from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save
from datetime import datetime,timedelta


class Author(models.Model):
    author_name = models.CharField(max_length=200)
    author_mail = models.EmailField(null=True)

    def __str__(self):
        return self.author_name


class Book(models.Model):
    book_name = models.CharField(max_length=200)
    availability = models.BooleanField(default=True)
    isbn = models.CharField(max_length=100)
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE)
    stock = models.IntegerField(default=1)
    total_books = models.IntegerField(default=1)

    def __str__(self):
        return self.book_name
    #
    # def get_author_mail_id(self):
    #     return self.author_name.author_mail


class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    member_name = models.CharField(max_length=200)
    contact = models.IntegerField()
    member_mail = models.EmailField()
    member_address = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.member_name


class Record(models.Model):
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    issue_date = models.DateField(default=datetime.now())
    return_date = models.DateField(default=datetime.now() + timedelta(days=7))
    member = models.ForeignKey(Member, on_delete=models.DO_NOTHING)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return self.book.book_name

    def member_name(self):
        return self.member.member_name

    def get_book_stock_availabilty(self):
        return self.book.availability

    def get_book_stock(self):
        return self.book.stock

@receiver(post_save, sender=Record)
def update_stock(sender,instance, created,**kwargs):
    book = instance.book
    if created:
        if book.availability == True:
            book.stock = book.stock - 1
        if book.stock == 0:
            book.availability = False
        book.save()


@receiver(pre_save, sender=Record)
def increment_stock(sender,instance,**kwargs):
    if not instance.returned:
        if any(Record.objects.filter(id=instance.id)):
            if Record.objects.get(id=instance.id).returned:
                instance.returned = True
    else:
        if Record.objects.get(id=instance.id).returned == False:
            book = instance.book
            book.stock = book.stock + 1
            if book.stock > 0:
                book.availability = True
            book.save()






