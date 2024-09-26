import requests

url = "https://thetestrequest.com/authors.xml"

res = requests.get(url=url)
if res.status_code == 200:
    print(res.text)
    with open("result.xml",'w',encoding='utf-8') as fp:
        fp.write(res.text)
else:
    print("invalid request")