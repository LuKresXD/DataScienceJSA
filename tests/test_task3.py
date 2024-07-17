import pytest
from flask import Flask, request, jsonify
from task3 import app, NotificationFactory


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_send_email_notification(client):
    response = client.post('/notifications', json={
        "type": "EmailNotification",
        "params": {
            "email": "test@lurkes.dev",
            "subject": "Test",
            "message": "This is a test email."
        }
    })
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data["status"] == "Email sent"


def test_send_sms_notification(client):
    response = client.post('/notifications', json={
        "type": "SMSNotification",
        "params": {
            "phone": "1234567890",
            "message": "This is a test SMS."
        }
    })
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data["status"] == "SMS sent"


def test_send_push_notification(client):
    response = client.post('/notifications', json={
        "type": "PushNotification",
        "params": {
            "device_id": "device123",
            "message": "This is a test push notification."
        }
    })
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data["status"] == "Push notification sent"


def test_unknown_notification_type(client):
    response = client.post('/notifications', json={
        "type": "UnknownNotif",
        "params": {
            "message": "Test123"
        }
    })
    json_data = response.get_json()
    assert response.status_code == 400
    assert "Unknown notification type" in json_data


if __name__ == "__main__":
    pytest.main()
