import pprint
import requests
from pymongo import MongoClient
import telegram
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

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
    url = f"https://openapi.naver.com/v1/search/shop.json?query={keyword}&display=10&sort=date&productType=3"
    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret}

    resp = requests.get(url, headers=headers)
    # 받아온 JSON 결과를 딕셔너리로 변환합니다.
    shopping_data = resp.json()

    # 검색 결과 중 items를 꺼내어 반환합니다.
    # pprint.pprint(shopping_data['items'])
    items = shopping_data['items']
    telephone = db.alerts.find_one({"telephone": phone})
    for item in items:
        lprice = int(item['lprice'])
        if lprice > price:
            print(item['link'], item['lprice'], item['mallName'])
            bot = telegram.Bot(token=chat_token)
            text = '♦️ ️최저가 알림 ♦️️' + '\n' + keyword + '를(을) 구매하실 때입니다!' + '\n\n' + '✔️판매가: ' + "{:,}".format(
                int(item['lprice'])) + '원' + '\n' + '✔️바로 확인하기: ' + item['link'] + '\n'
            bot.sendMessage(chat_id="1652157353", text=text)
#
#
# # scheduled > 매일 10시
#
# # User의 원하는 keyword를 검색해서 알림을 보내준다
# # 1. db에서 pushTarget 가져와서 Naver 쇼핑 keyword를 검색한다
# # 1-1. db.alerts에서 특정 column인 pushTarget을 변수화한다
# # 1-2. pushTarget를 검색 Keyword에 넣어서 검색한다
# # 2. 해당 Target에 low price를 db.alerts에서 가져온다
# # 2-1. User가 지정한 금액보다 적을 경우를 검색한다
# # 2-2. 적을 경우, Mallname,link,lprice를 가져온다
# # 2-3. 해당 User에게 알림을 보낸다
#
# # 3. telegram 이동 및 알림 버튼 클릭
# # Username: @intheshop_bot
#
#
# # 추가 챗봇으로 메세지를 하나 보내달라고 해서
# # 그게 전화번호랑 맞으면
# # 메세지를 보낼 때 그게 동일한지 확인하고 보내줌
#
#
# # 4. User 별로 알림 정보 나눠서 알림 보내주기
#
# # 5. 스케줄러 - 매일 오전 10시에 돌리기
