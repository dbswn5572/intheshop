import telegram

chat_token = "1671094125:AAGcJxhLg-HmGz-K4VRHWBT9xvl90ZwMjfE"
# chat = telegram.Bot(token = chat_token)
# updates = chat.getUpdates()
# for u in updates:
#     print(u.message['chat']['id'])

bot = telegram.Bot(token = chat_token)
text = '안녕하세요'
bot.sendMessage(chat_id = "1652157353", text=text)

image = 'static/IMG_1096.jpeg'
bot.send_photo(chat_id = '1652157353', photo=open(image, 'rb'))