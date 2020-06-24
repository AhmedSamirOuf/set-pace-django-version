from django.test import TestCase
from rest_framework import status
from rest_framework.utils import json

from .models import Book
from rest_framework.test import APIClient


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


class TestBookCrud(TestCase):
    BOOK_URL = '/api/book/'

    def setUp(self):
        self.api_client = APIClient()
        self.valid_book = {
            'title': 'harry potter and the deathly hallows',
            'author': 'J K Rowling',
            'category': 'fantasy',
            'publisher': 'ana',
            'vendor': ['ahram', 'akhbar', 'gmhorya'],
            'type': ['audio', 'paperbook', 'kindle'],
        }
        self.invalid_book = {
            'title': 'invalid',
            'author': '',
            'category': '',
            'publisher': 'ana',
        }

    def test_end_point_exist(self):
        response = self.api_client.post(self.BOOK_URL)
        self.assertNotEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid_book(self):
        response = self.api_client.post(self.BOOK_URL, data=json.dumps(self.valid_book), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, self.valid_book)

    def test_does_not_create_invalid_book(self):
        response = self.api_client.post(self.BOOK_URL, data=json.dumps(self.invalid_book), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

