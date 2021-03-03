import requests
import json

#1.
with open(r"/Users/yunju/sparta/intheshop/kakao_code.json", "r") as fp:
    tokens = json.load(fp)
    print(tokens)

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

# kapi.kakao.com/v2/api/talk/memo/default/send

headers = {
    "Authorization": "Bearer " + tokens["access_token"]
}

data = {
    "template_object": json.dumps({
        "object_type": "text",
        "text": "Hello, world!",
        "link": {
            "web_url": "www.naver.com"
        }
    })
}

response = requests.post(url, headers=headers, data=data)
response.status_code