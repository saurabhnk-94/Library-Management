from django.db import models

class Book(models.Model):
    book_name = models.CharField(max_length = 200)

    def __str__(self):
        return self.book_name

# Create your models here.
