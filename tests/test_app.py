import unittest

from src.app import sumar, multiplicar


class TestApp(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(sumar(2, 3), 5)

    def test_multiplicacion(self):
        self.assertEqual(multiplicar(2, 3), 6)


if __name__ == "__main__":
    unittest.main()