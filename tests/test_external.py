from unittest.mock import patch
from services.openfoodfacts import fetch_product

@patch("services.openfoodfacts.requests.get")
def test_fetch(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"status": 1}

    result = fetch_product("123")

    assert result["status"] == 1