import requests

print(
    requests.post(
        "http://0.0.0.0:10000",
        json={
            "query": "What is the most advanced language model by meta and why it is the most powerfull opensource model?",
        }
    ).json()
)