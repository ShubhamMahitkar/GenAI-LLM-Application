import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_generate_text(self):
        response = self.app.post('/generate', json={'prompt': 'Hello'})
        self.assertEqual(response.status_code, 200)

    def test_generate_text_empty_prompt(self):
        response = self.app.post('/generate', json={'prompt': ''})
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
