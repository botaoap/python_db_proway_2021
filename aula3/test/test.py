import unittest

class Test(unittest.TestCase):
    
    def test_something(self):
        assert 1 == 1
    
    def test_strings(self):
        assert "1" == "1"
    
    def test_boolean(self):
        assert True == True

    def test_booelan_two(self):
        a = "Test"
        assert bool(a)
    
    def test_many_tests(self):
        a = "Test"
        b = "Test"
        c = ""
        assert a == b or a == c

    def test_with_and(self):
        a = "Test"
        b = "Test"
        c = "Test"
        assert a == b and a == c
    
    def test_value_int(self):
        assert isinstance(1, int)

    
if __name__ == "__main__":
    unittest.main()
