# TODO: Recaptulando aula passada aula3/test/test.py

import unittest

class Test(unittest.TestCase):
    
    def test_with_and(self):
        a = "Test"
        b = "Test"
        c = ""
        assert a == b and a != c

    def test_int_values(self):
        assert isinstance(123456, int)
        assert isinstance("Sou uma string", str)
        assert isinstance(12.25, float)

    def test_with_not(self):
        a = "Test"
        b = "Test"
        c = ""

        assert a == b and not c
    
if __name__ == "__main__":
    unittest.main()
