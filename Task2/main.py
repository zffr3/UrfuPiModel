from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

@app.get("/nlp/{text}")
def analyse_text(text: str):
    pip = pipeline('sentiment-analysis', 'blanchefort/rubert-base-cased-sentiment')
    out = pip(text)
    return out