import unittest
from app import app

class TestHelloWorldAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_world(self):
        response = self.app.get('/hello')
        data = response.get_json()
        self.assertEqual(data['message'], "Hello World")
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
