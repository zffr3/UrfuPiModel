import json

from fastapi.testclient import TestClient
from Task2.main import app

client = TestClient(app)


def test_model():
    testData = {"привет":"NEUTRAL", "мне хорошо":"POSITIVE", "сегодня плохая погода":"NEGATIVE"}
    for key, value in testData.Items():
        url = "/nlp/"
        response = client.get(url, key)
        assert response.status_code == 200
        assert response.json()["label"] == value