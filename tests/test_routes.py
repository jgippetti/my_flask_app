import unittest
from app import my_app

class MathArtTestCase(unittest.TestCase):
    def setUp(self):
        self.app = my_app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'image/png')

if __name__ == '__main__':
    unittest.main()