import requests

req = requests.get("https://api.opensea.io/api/v1/assets")

print(req.json())