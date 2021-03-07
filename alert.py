import pprint
import requests
from pymongo import MongoClient
import telegram

chat_token = "1671094125:AAGcJxhLg-HmGz-K4VRHWBT9xvl90ZwMjfE"
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.intheshop


push_list = list(db.alerts.find({}, {'_id': False}))
print(push_list)

for push in push_list:
    price = int(push['pushLow'])
    phone = push['pushNum']

    # API info
    client_id = "Xwl1iOsmsp0RJjJImyvr"
    client_secret = "ZLaBm7BkGg"
    keyword = push['pushTarget']
    url = "https://openapi.naver.com/v1/search/shop.json?query={keyword}&display=30&sort=date"
    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret}

    resp = requests.get(url, headers=headers)
    # 받아온 JSON 결과를 딕셔너리로 변환합니다.
    shopping_data = resp.json()

    # 검색 결과 중 items를 꺼내어 반환합니다.
    #pprint.pprint(shopping_data['items'])
    items = shopping_data['items']
    for item in items:
        lprice = int(item['lprice'])
        print(item)
        if lprice < price:
            print(item['link'], item['lprice'], item['mallName'])
            #bot = telegram.Bot(token=chat_token)
            #text = '♦️최저가 알림♦️'+'\n'+ '제품명:' + item['title'] + '\n' + '링크이동:' + item['link'] + '\n'+ '가격:' + item['lprice']
            #bot.sendMessage(chat_id="1652157353", text=text)
            #  '<뽐뿌 게시글 업데이트>'+'\n'+title+'\n'+link



# scheduled > 매일 10시
# User의 원하는 keyword를 검색해서 알림을 보내준다
# 1. db에서 pushTarget 가져와서 Naver 쇼핑 keyword를 검색한다
# 1-1. db.alerts에서 특정 column인 pushTarget을 변수화한다
# 1-2. pushTarget를 검색 Keyword에 넣어서 검색한다
# 2. 해당 Target에 low price를 db.alerts에서 가져온다
# 2-1. User가 지정한 금액보다 적을 경우를 검색한다
# 2-2. 적을 경우, Mallname,link,lprice를 가져온다
# 2-3. 해당 User에게 카카오톡 알림을 보낸다



