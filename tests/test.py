from main import main
import unittest

class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(), "10 Academy")
        print("Test passsed")  

if __name__ == '_main_':
    unittest.main()        