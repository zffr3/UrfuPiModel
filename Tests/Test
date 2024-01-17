import json
import requests

URL = 'http://127.0.0.1:8000'

testData = {"привет":"NEUTRAL", "мне хорошо":"POSITIVE", "сегодня плохая погода":"NEGATIVE"}

def test_model():
    for key, value in testData.Items():
        response = requests.get(f"{URL}/nlp/{key}")
        assert requests.status_code == 200
        assert requests.json()["label"] == value