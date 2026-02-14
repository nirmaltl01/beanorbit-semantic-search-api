import sys
import os
from fastapi.testclient import TestClient

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.main import app

client = TestClient(app)

def test_query_success():
    response = client.post("/query", json={
        "query": "What services does BeanOrbit offer?"
    })

    assert response.status_code == 200
    data = response.json()

    assert "results" in data
    assert len(data["results"]) > 0
    assert "services" in data["results"][0]["content"].lower()


def test_query_empty():
    response = client.post("/query", json={
        "query": ""
    })

    assert response.status_code == 400
