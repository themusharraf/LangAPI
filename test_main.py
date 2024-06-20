from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home_page():
    request = client.get("/")
    assert request.status_code == 200
    assert request.json() == {"message": "EN / UZ lang endpoint"}


def test_uz_en():
    request = client.get('/uz_en/maktab')  # noqa
    assert request.status_code == 200
    assert request.json() == {"EN": "school"}


def test_en_uz():
    request = client.get("/en_uz/hello")
    assert request.status_code == 200
    assert request.json() == {"UZ": "salom"}
