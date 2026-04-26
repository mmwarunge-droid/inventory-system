import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_get_inventory(client):
    response = client.get("/inventory")
    assert response.status_code == 200

def test_add_item(client):
    response = client.post("/inventory", json={
        "product_name": "Juice",
        "brands": "Minute Maid",
        "price": 300,
        "stock": 10,
        "barcode": "222"
    })

    assert response.status_code == 201