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
