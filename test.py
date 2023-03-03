import requests
r=requests.get("localhost:8080/images")
print(r.text)