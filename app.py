import requests
import pprint
import telegram
import json
import re

from flask import render_template, Flask, request, jsonify, Response, send_file
from pymongo import MongoClient
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

app = Flask(__name__)

# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.intheshop

chat_token = "1671094125:AAGcJxhLg-HmGz-K4VRHWBT9xvl90ZwMjfE"
updater = Updater(chat_token)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/pushlist')
def pushlist():
    return render_template('pushlist.html')


@app.route('/push', methods=['POST'])
def write_alert():
    target_receive = request.form['target_give']
    price_receive = request.form['price_give']
    phone_receive = request.form['phone_give']
    print(target_receive, price_receive, phone_receive)

    doc = {
        'pushTarget': target_receive,
        'pushLow': price_receive,
        'pushNum': phone_receive
    }
    db.alerts.insert_one(doc)

    return jsonify({'result': 'success', 'msg': 'Telegram으로 알림 받으러 가보실께요!'})


# check for SSL
@app.route('/.well-known/pki-validation/6D2F02CED5234B9456BE852E09278754.txt')
def certi():
    return send_file("static/6D2F02CED5234B9456BE852E09278754.txt")


# Telegram start
# https://api.telegram.org/bot1671094125:AAGcJxhLg-HmGz-K4VRHWBT9xvl90ZwMjfE/getMe
# https://api.telegram.org/bot1671094125:AAGcJxhLg-HmGz-K4VRHWBT9xvl90ZwMjfE/sendMessage?chat_id=1652157353&text=api test
# https://api.telegram.org/bot1671094125:AAGcJxhLg-HmGz-K4VRHWBT9xvl90ZwMjfE/setWebhook?url=https://intheshop-push.shop/telegram

# def write_json(data, filename='response.json'):
#     with open(filename, 'w') as f:
#         json.dump(data, f, indent=4, ensure_ascii=False)
def sendMessage(chat_id, text):
    url = f'https://api.telegram.org/bot1671094125:AAGcJxhLg-HmGz-K4VRHWBT9xvl90ZwMjfE/sendMessage'
    payload = {'chat_id': chat_id, 'text': text}

    r = requests.post(url, json=payload)
    return r


@app.route('/telegram', methods=['POST', 'GET'])
def start():
    """
    동일한 사용자에게 응답 할 수 있도록 chat_id 가져 오기
    """
    data = request.get_json()
    print(data)
    chat_id = data['message']['chat']['id']
    text = data['message']['text']

    if text == r'/start':
        txt = 'intheshop에 알림을 등록해주셔서 감사합니다!' + '\n\n' + '💌intheshop-push.shop💌 에서 등록한!' + '\n' + '연락처를 입력해주세요!(형식: 01012345678)' + '\n\n' + '등록한 정보가 다를 경우 알림을 보내드릴 수 없습니다ㅠ-ㅠ'
        sendMessage(chat_id, txt)
    else:
        sendMessage(chat_id, text)

    return json.dumps({'success': True})
    # return '', 200

    # chat_id = update.message.chat.id
    # msg_id = update.message.message_id
    # update.message.reply_text(
    #     '안녕하세요, intheshop에 알림을 등록해주셔서 감사합니다!' + '\n\n' + '💌intheshop-push.shop💌 에서 등록한!' + '\n' + '연락처를 입력해주세요!(형식: 01012345678)' +
    # start_handler = CommandHandler('start', start)
    # updater.dispatcher.add_handler(start_handler)
    # updater.start_polling(timeout=3, clean=True)
    # updater.idle()


@app.route('/telephone', methods=['POST'])
def get_info(update, context):
    """
    핸드폰 번호 확인!
    # update.message.reply_text('💌intheshop-push.shop💌 에서 등록한 연락처를 입력해주세요!')
    """
    info_handler = MessageHandler(Filters.text, get_info)
    updater.dispatcher.add_handler(info_handler)
    updater.start_polling(timeout=3, clean=True)
    updater.idle()
    telephone = update.message.text
    if telephone is not None:
        print(telephone)
        update.message.reply_text('감사합니다!' + '\n\n' + '최저가 딜이 등록되면 알림 드리겠습니다👌🏼')
    db.alerts.update_one({'pushNum': telephone}, {'$set': {'telephone': telephone}})


def alert():
    push_list = list(db.alerts.find({}, {'_id': False}))
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
        print(telephone, phone)

        for item in items:
            lprice = int(item['lprice'])
            if lprice > price and phone == telephone:
                print(item['link'], item['lprice'], item['mallName'])
                bot = telegram.Bot(token=chat_token)
                text = '♦️ ️최저가 알림 ♦️️' + '\n' + keyword + '를(을) 구매하실 때입니다!' + '\n\n' + '✔️판매가: ' + "{:,}".format(
                    int(item['lprice'])) + '원' + '\n' + '✔️바로 확인하기: ' + item['link'] + '\n'
                bot.sendMessage(chat_id="1652157353", text=text)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
