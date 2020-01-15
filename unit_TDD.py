import unittest
from fb import FizzBuzz


class Tf(unittest.TestCase):
    def test_aa(self):
        self.assertEquals(FizzBuzz(1), 1)
        self.assertEquals(FizzBuzz(3), 'Fizz')
        self.assertEquals(FizzBuzz(5), 'Buzz')
        self.assertEquals(FizzBuzz(15), 'FizzBuzz')


if __name__ == '__main__':
    unittest.main()
