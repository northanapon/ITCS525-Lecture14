import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_test_db_endpoint():
    """
    Test the /test-db endpoint to ensure database connectivity.
    """
    response = client.get("/test-db")
    assert response.status_code == 200
    data = response.json()
    assert "db_result" in data, f"Unexpected response: {data}"
    assert data["db_result"] == 1