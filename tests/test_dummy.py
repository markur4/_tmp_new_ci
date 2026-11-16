"""Tests for the repository's dummy CI example."""

import unittest

from ci_probe import add


class AddTests(unittest.TestCase):
    def test_adds_two_integers(self) -> None:
        self.assertEqual(add(20, 22), 42)


if __name__ == "__main__":
    unittest.main()
