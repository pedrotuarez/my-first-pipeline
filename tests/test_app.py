import unittest

from src.app import sumar


class TestApp(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(sumar(2, 3), 5)


if __name__ == "__main__":
    unittest.main()