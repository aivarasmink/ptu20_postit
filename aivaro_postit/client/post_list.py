import http.client
import json

conn = http.client.HTTPConnection("127.0.0.1", 8000)

headersList = {
 "Accept": "*/*",
 "User-Agent": "PTU20 API browser" 
}

payload = ""

conn.request("GET", "/", payload, headersList)
response = conn.getresponse()
result = response.read()
data = json.loads(result)

for post in data:
    for key, value in post.items():
        print(f"{key}: {value}")
