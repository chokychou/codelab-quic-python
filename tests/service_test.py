import unittest
import httpx

from fastapi.testclient import TestClient
from src.fastapi.service import app


class TestGetNumber(unittest.TestCase):

    client = TestClient(app)

    def test_read_main(self):
        response = self.client.get("/api/logs/")
        assert response.status_code == 200
        print(response.json())
        assert response.json() == {"message": "logs root endpoint"}


if __name__ == "__main__":
    unittest.main()
