import unittest
import os
from app.modelDB import init_db
from app.api import app

class APITestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        if os.path.exists("crypto.db"):
            os.remove("crypto.db")
        init_db()

    def test_get_prices_empty(self):
        response = self.app.get('/prices')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])

    def test_add_price(self):
        response = self.app.post('/prices', json={'name': 'Bitcoin', 'value': 30000.0})
        self.assertEqual(response.status_code, 200)

        # Comprueba que se añadió correctamente
        response = self.app.get('/prices')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [{'name': 'Bitcoin', 'value': 30000.0}])


