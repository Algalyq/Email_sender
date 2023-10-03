# test_main.py
import pytest
from fastapi.testclient import TestClient
from main import app
from configs.config import MailBody

client = TestClient(app)
BASE_URL = "http://localhost:8080"

@pytest.fixture
def sample_mail_data():
    return {
        "to": "recipient@example.com",
        "subject": "Testing 1",
        "body": "Testing body 1"
    }

def test_send_mail_success(sample_mail_data):
    response = client.post(f"{BASE_URL}/send-email", json=sample_mail_data)
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_index():
    response = client.get(f"{BASE_URL}/")
    assert response.status_code == 200
    assert response.json() == {"status": "fastapi mailserver is running."}
