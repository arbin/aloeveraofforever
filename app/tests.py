"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


def add_entry():
    from app.models import AlternativeMedicine
    entry = AlternativeMedicine(name = 'guyabano',
            scientific_name = 'guyabanosis',
            description = 'a cancer killer',
            locally_grown = 1,
            imported_products = 0,
            intake = 1,
            topical = 0,
            related_website = 'http://aaa.com',
            image = '',
            date_added = '')


