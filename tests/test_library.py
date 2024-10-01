import unittest
from unittest.mock import Mock
from library import library
import json

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = library.Library()
        with open('tests_data/ebooks.txt', 'r') as source:
            self.books_data = json.loads(source.read())
    def test_is_ebook_return_true(self):
        self.library.api.get_ebooks = Mock(return_value=self.books_data)
        self.assertTrue(self.library.is_ebook('Aprendendo Python'))

    def test_is_ebook_return_false(self):
        self.library.api.get_ebooks = Mock(return_value=self.books_data)
        self.assertFalse(self.library.is_ebook('War and Peace'))