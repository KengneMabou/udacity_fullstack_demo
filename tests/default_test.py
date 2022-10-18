from core import app
from models import *
from controllers import *
from models.sqlalchemy_init import db
import unittest

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/test_db'


class ResourceTestCase(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client()

    def tearDown(self):
        """Executed after each test"""
        pass

    def test_given_behavior(self):
        """Test _____________ """
        res = self.client().get('/')
        self.assertEqual(res.status_code, 200)