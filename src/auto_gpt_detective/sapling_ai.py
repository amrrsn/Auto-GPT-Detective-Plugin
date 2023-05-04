import os
import requests
import json


def _sapling_detect(text: str, sent_scores: bool = False) -> str:
    api_key = os.getenv("SAPLINGAI_API_KEY")
    post_endpoint = os.getenv("SAPLINGAI_POST_ENDPOINT")
    if post_endpoint is None:
        post_endpoint = "https://api.sapling.ai/api/v1/aidetect"

    body = {
        "key": api_key,
        "text": text,
        "sent_scores": sent_scores
    }

    response = requests.post(post_endpoint, json=body)
    response.raise_for_status()

    results = response.json()
    return json.dumps(results, ensure_ascii=False, indent=4)


sapling_post_endpoint = 'https://api.sapling.ai/api/v1/aidetect'


class SaplingAIDetector:
    def __init__(self, api_key: str, post_endpoint: str = sapling_post_endpoint):
        self.api_key = api_key
        self.post_endpoint = post_endpoint

    def detect(self, text: str, sent_scores: bool = False) -> dict:
        body = {
            'key': self.api_key,
            'text': text,
            'sent_scores': sent_scores
        }

        response = requests.post(self.post_endpoint, json=body)
        return response.json()
