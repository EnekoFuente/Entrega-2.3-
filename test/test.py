import unittest
import json
from app.api import api_bp
from app import models
from flask import Flask

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(api_bp)
        self.client = self.app.test_client()

        models.DB_PATH = ':memory:'
        models.init_db()

    def test_get_prices_empty(self):
        response = self.client.get('/prices')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data, [])

    def test_add_price(self):
        new_price = {'name': 'BTC', 'value': 32000}
        response = self.client.post('/prices',
                                    data=json.dumps(new_price),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/prices')
        data = json.loads(response.data)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], 'BTC')
        self.assertEqual(data[0]['value'], 32000)

if __name__ == '__main__':
    unittest.main()

