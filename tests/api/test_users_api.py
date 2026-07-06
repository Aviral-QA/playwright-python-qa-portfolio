import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_single_user():
    response = requests.get(f"{BASE_URL}/users/2")
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 2
    assert "email" in data
    assert "name" in data


def test_get_user_not_found():
    response = requests.get(f"{BASE_URL}/users/999")
    assert response.status_code == 404


def test_create_user():
    payload = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "job": "QA Engineer"
    }
    response = requests.post(f"{BASE_URL}/users", json=payload)
    assert response.status_code == 201

    data = response.json()
    assert data["name"] == "John Doe"
    assert data["email"] == "john.doe@example.com"
    assert "id" in data


def test_update_user():
    payload = {
        "name": "John Doe",
        "job": "Senior QA Engineer"
    }
    response = requests.put(f"{BASE_URL}/users/2", json=payload)
    assert response.status_code == 200

    data = response.json()
    assert data["job"] == "Senior QA Engineer"


def test_delete_user():
    response = requests.delete(f"{BASE_URL}/users/2")
    assert response.status_code == 200