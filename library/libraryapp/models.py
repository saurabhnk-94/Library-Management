from django.db import models


class Author(models.Model):
    author_name = models.CharField(max_length=200)
    author_mail = models.EmailField()

    def __str__(self):
        return self.author_name +'-'+ self.author_mail


class Book(models.Model):
    book_name = models.CharField(max_length=200)
    availability = models.BooleanField(default=True)
    isbn = models.CharField(max_length=100)
    author_obj = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.book_name + '-' + self.isbn


class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    member_name = models.CharField(max_length=200)
    contact = models.IntegerField()

    def __str__(self):
        return self.member_name + '-' + str(self.contact)

# class Records(models.Model):
#     book_object = models.ForeignKey(Book, null = True, on_delete = models.CASCADE)
#     issue_date = models.DateField()
#     return_date = models.DateField()
#
#
#     def book_details(self):
#         return
#

