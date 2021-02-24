import requests
import pprint

from flask import render_template, Flask
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.intheshop

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Naver Search - Shopping API
client_id = "Xwl1iOsmsp0RJjJImyvr"
client_secret = "ZLaBm7BkGg"

# API info
keyword = '요가'
url = f"https://openapi.naver.com/v1/search/shop.json?query={keyword}&display=10"

print(url)

# 아이디와 시크릿 키를 부가 정보로 같이 보냅니다.
headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
# 검색 결과를 data에 저장합니다.
resp = requests.get(url, headers=headers)
# 받아온 JSON 결과를 딕셔너리로 변환합니다.
data = resp.json()
# 검색 결과 중 items를 꺼내어 반환합니다.
pprint.pprint(data)

