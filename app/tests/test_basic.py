import unittest

from app.main import app


class BasicTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_root(self):
        resp = self.app.get('/')
        assert b'Hello world!' in resp.data
