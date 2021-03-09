import telegram
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

# chat_token = "1671094125:AAGcJxhLg-HmGz-K4VRHWBT9xvl90ZwMjfE"


# bot = telegram.Bot(token=chat_token)
# text = '♦️ ️최저가 알림 ♦️️'+'\n'+ keyword + '를(을) 구매하실 때입니다!' + '\n\n' + '✔️판매가: ' + "{:,}".format(int(item['lprice']))+ '원' +  '\n' + '✔️바로 확인하기: ' + item['link'] + '\n'
# bot.sendMessage(chat_id="1652157353", text=text)




#
# def get_message(update, context):
#     telephone = update.message.text
#     print(telephone)
#     # 여기에 핸드폰 번호가 동일하면 밑에 메세지 보내도록 설정 필요
#     update.message.reply_text('감사합니다!'+ '\n\n'+'최저가 딜이 등록되면 알림 드리겠습니다👌🏼')
#

#
# # message reply function
# def get_message(update, context):
#     # update.message.reply_text("got text")
#     # 핸드폰 번호 입력받아서 pushNum이랑 비교해 010-XXXX-XXXX
#     # 같으면 그 keyword만 api 돌려서 알림 보내줘
#
#     update.message.reply_text(update.message.text)
#     print(update.message.text)
#
#
# # help reply function
# def help_command(bot, update):
#     update.message.reply_text("무엇을 도와드릴까요?")





# photo_handler = MessageHandler(Filters.photo, get_photo)
# updater.dispatcher.add_handler(photo_handler)
# file_handler = MessageHandler(Filters.document, get_file)
# updater.dispatcher.add_handler(file_handler)

