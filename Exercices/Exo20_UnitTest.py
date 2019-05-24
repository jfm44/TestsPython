
import unittest

class TestCreateLifo(unittest.TestCase):
    def testString(self):
        a = "UneChaine"
        b = "UneChaine"
        self.assertEqual(a,b)
        
    def testBool (self):
        a = True
        b = False
        self.assertEqual(a,b)

if __name__ == "__main__":
    unittest.main()
