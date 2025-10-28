def test_fastapi_main():
    assert True

from fastapi.testclient import TestClient
from fastapi_main import app
import pytest
from typing import Dict, List, Union

client = TestClient(app)

@pytest.fixture
def valid_request_data() -> Dict:
    return {
        "num_exam": 1,
        "language_level": "B2",
        "students": 2,
        "dict_list_values": {
            "Name": ["Student 1", "Student 2"],
            "Reading": ["40/50", "45/50"],
            "Listening": ["35/40", "38/40"],
            "Writing": ["25/30", "27/30"],
            "Speaking": ["20/25", "22/25"],
            "Use_English": ["35/40", "37/40"]
        }
    }

def test_root_endpoint():
    """Prueba el endpoint raíz"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API is running"}

def test_get_files_valid_data(valid_request_data):
    """Prueba el endpoint get_files con datos válidos"""
    response = client.post("/get_files", json=valid_request_data)
    if response.status_code != 200:
        print(f"Error response: {response.json()}")
        print(f"Request data: {valid_request_data}")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/octet-stream"


def test_get_files_invalid_language_level():
    """Prueba el endpoint con un nivel de idioma inválido"""
    invalid_data = {
        "num_exam": 1,
        "language_level": "InvalidLevel",
        "students": 2,
        "dict_list_values": {
            "Name": ["Student 1"],
            "Reading": ["40/50"],
            "Listening": ["35/40"],
            "Writing": ["25/30"],
            "Speaking": ["20/25"],
            "Use_English": ["35/40"]
        }
    }
    response = client.post("/get_files", json=invalid_data)
    assert response.status_code == 400

def test_get_files_empty_dict():
    """Prueba el endpoint con un diccionario vacío"""
    empty_data = {
        "num_exam": 1,
        "language_level": "B2",
        "students": 0,
        "dict_list_values": {}
    }
    response = client.post("/get_files", json=empty_data)
    assert response.status_code == 400