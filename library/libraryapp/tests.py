from django.test import TestCase
from libraryapp.models import *


class RecordTestCases(TestCase):
    def setUp(self):
        """to create a virtual database and to add details"""
        author = Author.objects.create(author_name='Vishal Mane',author_mail='vishal@gmail.com')
        Book.objects.create(book_name='Clean Code',isbn='7362-1162-111',author_name=author,stock=5,total_books=10)
        Member.objects.create(member_name='Sachin',contact='9763152521',member_mail='sa@gmail.com',
                              member_address='Bangalore')
        # Record.objects.create(book=book,member=member)

    def test_case_get_member_name(self):
        """to test the particular function"""
        book = Book.objects.get(book_name='Clean Code')
        member = Member.objects.get(member_name='Sachin')
        record = Record.objects.create(book = book, member=member)
        self.assertEqual(record.member_name(), 'Sachin')

    def test_case_get_availabilty(self):
        """check the availability in the stock if issued"""
        book = Book.objects.get(book_name='Clean Code')
        member = Member.objects.get(member_name='Sachin')
        record = Record.objects.create(book=book, member=member)
        self.assertEqual(record.get_book_stock_availabilty(), True)


    def test_case_get_stock(self):
        '''Check the difference in stock'''
        book = Book.objects.get(book_name='Clean Code')
        member = Member.objects.get(member_name='Sachin')
        initial_stock = book.stock
        Record.objects.create(book=book, member=member)
        final_stock = book.stock
        self.assertEqual(initial_stock-final_stock, 1)