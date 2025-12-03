import requests
import os

BACKEND_URL = os.getenv("BACKEND_URL")

def ping_backend():
    try:
        response = requests.get(BACKEND_URL, timeout=10)
        print(f"Ping successful → Status: {response.status_code}")
    except Exception as e:
        print("Ping failed:", e)

if __name__ == "__main__":
    ping_backend()
