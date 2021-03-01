import pprint
import requests

client_id = "Xwl1iOsmsp0RJjJImyvr"
client_secret = "ZLaBm7BkGg"

# API info
keyword = '요가링 안다'
url = "https://openapi.naver.com/v1/search/shop.json?query={keyword}&display=30&sort=date"
headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret}

# 검색 결과를 data에 저장합니다.
resp = requests.get(url, headers=headers)
# 받아온 JSON 결과를 딕셔너리로 변환합니다.
shopping_data = resp.json()

# 검색 결과 중 items를 꺼내어 반환합니다.
pprint.pprint(shopping_data['items'])
items = shopping_data['items']

for item in items:
    if item['lprice'] > '5000':
        print(item['link'], item['lprice'], item['mallName'])