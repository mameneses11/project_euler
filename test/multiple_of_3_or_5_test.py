import unittest
from src.multiple_of_3_or_5 import example, implementation


class MultipleOf3Or5(unittest.TestCase):
    def test_example(self) -> None:
        self.assertIsInstance(example(), int)
        self.assertEqual(23, example())

    def test_implementation(self) -> None:
        self.assertIsInstance(implementation(), int)
        self.assertEqual(233168, implementation())



if __name__ == '__main__':
    unittest.main()
