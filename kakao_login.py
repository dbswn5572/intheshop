# import requests
#
# url = 'https://kauth.kakao.com/oauth/token'
# rest_api_key = '7d0131eddc179284be65194d6d8ebb5e'
# redirect_uri = 'https://example.com/oauth'
# authorize_code = 'eAQVen8TaSXfBhreNwtmcUWrcHADU8FWQYK-UuMSjDL7AWYBi6_7k2QfvCy36aX5Duiiygo9cusAAAF39hy5xA'
#
# data = {
#     'grant_type':'authorization_code',
#     'client_id':rest_api_key,
#     'redirect_uri':redirect_uri,
#     'code': authorize_code,
#     }
#
# response = requests.post(url, data=data)
# tokens = response.json()
# print(tokens)
#
# # json 저장
# import json
# #1.
# with open(r"/Users/yunju/sparta/intheshop/kakao_code.json","w") as fp:
#     json.dump(tokens, fp)
#
# # #2.
# # with open("kakao_code.json","w") as fp:
# #     json.dump(tokens, fp)

# json 읽어오기
import json
#1.
with open(r"/Users/yunju/sparta/intheshop/kakao_code.json","r") as fp:
    ts = json.load(fp)
print(ts)
print(ts["access_token"])

