from django.db import models

class Author(models.Model):
    author_fname = models.CharField(max_length = 200)
    author_lname = models.CharField(max_length=200)

    def __str__(self):
        return self.author_fname +' '+self.author_lname

    def full_name(self):
        return '{} {}'.format(self.author_fname,self.author_lname).upper()


class Book(models.Model):
    book_name = models.CharField(max_length = 200)
    book_price = models.IntegerField(default = 0)
    availability = models.BooleanField(default = True)
    isbn = models.CharField(max_length = 100)
    author_name = models.ForeignKey(Author, null=True, on_delete =models.CASCADE)



    def __str__(self):
        return self.book_name + '-' + str(self.book_price) + self.isbn

    def upper_name(self):
        return self.book_name.upper()

# Create your models here.
