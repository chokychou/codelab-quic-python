import unittest
import httpx

from falcon import testing
from src.service import api_router


class MyTestCase(testing.TestCase):
    def setUp(self):
        super(MyTestCase, self).setUp()
        self.app = api_router


class TestMyApp(MyTestCase):
    def test_get_message(self):
        doc = {"message": "hello smartass"}

        result = self.simulate_get("/hello/smartass")
        self.assertEqual(result.json, doc)


if __name__ == "__main__":
    unittest.main()
