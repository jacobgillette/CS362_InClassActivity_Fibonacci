import unittest
import fib


class TestCase(unittest.TestCase):

    def test_fib(self):
        self.assertEqual(fib.fib(1), 0)

    def test_fib1(self):
        self.assertEqual(fib.fib(10),34)

    def test_fib2(self):
        self.assertEqual(fib.factorial(1),1)

if __name__ == '__main__':
    unittest.main(verbosity=2)
