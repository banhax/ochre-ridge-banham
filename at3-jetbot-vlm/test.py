import requests

req = requests.post("http://172.20.20.16:5000/", data={"content":"hello world"})
print(req.text)