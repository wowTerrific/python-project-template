import unittest

from hello.hello import Hello

class TestHello(unittest.TestCase):
    def test_sayName(self):
        hello = Hello("john")
        hello.say_hello()
        self.assertEqual(hello.whats_my_name(), "john", "name isn't correct")
        
    def test_nothing(self):
        self.assertEqual(1+1, 2, "eyeyeye")


if __name__ == "__main__":
    unittest.main()