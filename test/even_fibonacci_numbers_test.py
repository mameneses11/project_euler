import unittest
from src.even_fibonacci_numbers import example, implementation


class EvenFibonacciNumbers(unittest.TestCase):
    def test_example(self) -> None:
        self.assertIsInstance(example(), int)
        self.assertEqual(44, example())

    def test_implementation(self) -> None:
        self.assertIsInstance(implementation(), int)
        self.assertEqual(4_613_732, implementation())


if __name__ == '__main__':
    unittest.main()
