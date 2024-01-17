import json

from fastapi.testclient import TestClient
from Task2.main import app

client = TestClient(app)

def test_model():
    testData = {"привет":"NEUTRAL", "мне хорошо":"POSITIVE", "сегодня плохая погода":"NEGATIVE"}
    for key in testData:
        url = "/nlp/"
        response = client.get(f'{url}{key}', headers={"X-Token": "coneofsilence"})
        assert response.status_code == 200
        assert response.json()[0]["label"] == testData[key]