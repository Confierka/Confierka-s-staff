import requests

resp = requests.get('http://localhost:8000/')

print(resp.status_code)
print(resp.text)
print(resp.headers)
