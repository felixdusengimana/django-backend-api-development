from django.test import TestCase

from .calc import add, subtract


class CalcTests(TestCase):
    def test_add_numbers(self):
        """Test that two numbers are used together."""
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """Testing that values are subtracted."""
        self.assertEqual(subtract(7, 11), 4)