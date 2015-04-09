import unittest
from series import fibonacci, lucas

class MyTests(unittest.TestCase):

    def test_fib(self):

        assert fibonacci(-1) == None
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1
        assert fibonacci(5) == 5
        assert fibonacci(10) == 55

    def test_lucas(self):
        assert lucas(-14) == None
        assert lucas(0) == 2
        assert lucas(1) == 1
        assert lucas(6) == 18

if __name__ == "__main__":
    unittest.main()
