import requests
import pprint

from flask import render_template, Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.intheshop


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pushlist')
def pushlist():
    return render_template('pushlist.html')


@app.route('/push', methods=['POST'])
def write_alert():
    # 'target_give': target,
    #                     'price_give': price,
    #                     'phone_give': phone
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

    return jsonify({'result': 'success', 'msg': '알림 요청이 완료되었습니다. \n희망가 등록 시 알림드릴께요 🥰'})


def crawl(keyword):
    client_id = "Xwl1iOsmsp0RJjJImyvr"
    client_secret = "ZLaBm7BkGg"

    # API info
    keyword = '요가링 안다'
    url = f"https://openapi.naver.com/v1/search/shop.json?query={keyword}&display=10"
    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret}

    # 검색 결과를 data에 저장합니다.
    resp = requests.get(url, headers=headers)
    # 받아온 JSON 결과를 딕셔너리로 변환합니다.
    shopping_data = resp.json()
    # 검색 결과 중 items를 꺼내어 반환합니다.
    items = shopping_data['items']
    pprint.pprint(shopping_data)
    for item in items:
        if int(item['lprice']) > 0:
            print(item['link'], item['lprice'], item['mallName'])


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)







