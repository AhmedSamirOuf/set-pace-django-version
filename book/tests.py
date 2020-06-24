from django.test import TestCase
from .models import Book


class TestBookModel(TestCase):

    def set_test_param(self, param):
        self.test_param = param

    def test_book_has_a_title(self):
        self.set_test_param('test_book')
        book = Book(title=self.test_param)
        self.assertEqual(book.title, self.test_param)

    def test_book_has_author(self):
        self.set_test_param('test_author')
        book = Book(author=self.test_param)
        self.assertEqual(book.author, self.test_param)

    def test_book_has_publisher(self):
        self.set_test_param('test_publisher')
        book = Book(publisher=self.test_param)
        self.assertEqual(book.publisher, self.test_param)

    def test_book_has_vendors(self):
        self.set_test_param(['test_vendor1', 'test_vendor2'])
        book = Book(vendors=self.test_param)
        self.assertEqual(book.vendors, self.test_param)

    def test_book_has_types(self):
        self.set_test_param(['test_type1', 'test_type2'])
        book = Book(types=self.test_param)
        self.assertEqual(book.types, self.test_param)

    def test_book_has_category(self):
        self.set_test_param('test_category')
        book = Book(category=self.test_param)
        self.assertEqual(book.category, self.test_param)
