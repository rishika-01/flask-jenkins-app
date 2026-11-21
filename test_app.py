import unittest
from app import app

class FlaskAppTest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_homepage(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Hello from Flask!")

if __name__ == "__main__":
    unittest.main()