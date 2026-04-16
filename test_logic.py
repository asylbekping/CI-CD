import unittest

def check_even(number):
    return number % 2 == 0

class TestLogic(unittest.TestCase):
    def test_is_even(self):
        self.assertTrue(check_even(4))
    
    def test_is_odd(self):
        self.assertFalse(check_even(3))

if __name__ == "__main__":
    unittest.main()

