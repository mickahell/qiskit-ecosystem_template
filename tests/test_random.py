"""Docstring."""
import unittest

from src import Random


class TestRandom(unittest.TestCase):
    """Tests Random class implementation."""

    def test_run(self):
        """Tests run method random."""
        random = Random()

        self.assertEqual(random.run(2), 4)
