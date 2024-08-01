import unittest
from yeonji.module1 import formatted_name


class MyTestCase(unittest.TestCase):
    def test_something(self):
        first = formatted_name('yeonji', 'oh')
        print(first)
        self.assertEqual(first, 'Yeonji Oh')  # add assertion here


if __name__ == '__main__':
    unittest.main()
