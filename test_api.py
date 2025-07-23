import requests

# Payload to send
payload = {
    "bank": "HDFC",
    "card_type": "Credit",
    "order_amount": 6000
}

# Make POST request to your FastAPI offer endpoint
response = requests.post("http://127.0.0.1:8000/offer", json=payload)

# Print the response from the API
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
