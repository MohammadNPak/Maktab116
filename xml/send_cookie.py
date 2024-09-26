import requests

cookie={"session_id":"abc"}
res = requests.get('http://10.20.30.28:8000',cookies=cookie)
if res.status_code==200:
    print(res.json())
