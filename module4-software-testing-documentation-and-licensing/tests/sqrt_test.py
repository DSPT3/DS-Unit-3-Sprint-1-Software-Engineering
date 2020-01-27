import unittest
from sqrt import newton_sqrt1, newton_sqrt2, lazy_sqrt, builtin_sqrt

class SqrtTests(unittest.TestCase):
    ''' Obligatory docstring, test square root functions! '''
    def test_sqrt(self):
        self.assertEqual(lazy_sqrt(9), 3)

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)