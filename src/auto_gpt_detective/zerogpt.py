import os
import requests
import json


def _zerogpt_detect(text: str) -> str:
    post_endpoint = os.getenv("ZEROGPT_POST_ENDPOINT")
    if post_endpoint is None:
        post_endpoint = "https://api.zerogpt.com/api/detect/detectText"

    header_json_path = os.getenv("ZEROGPT_HEADER_JSON_PATH")
    if header_json_path is None:
        return "ERROR: Due to ZeroGPT's implementation, \
               a json file defining the POST headers \
               is required to proceed"

    with open(header_json_path, "r") as header_json:
        head = json.loads(header_json.read())

    body = {
        "input_text": text,
    }

    response = requests.post(post_endpoint, headers=head, json=body)
    response.raise_for_status()

    results = response.json()

    if results['success']:
        rdata = results['data']
        rdata.pop('hi', None)
        rdata.pop('input_text', None)
        results = rdata

    return json.dumps(results, ensure_ascii=False, indent=4)
