import unittest
from app import add  # Adjust this import based on your actual function

class TestApp(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)

if __name__ == '__main__':
    unittest.main()

