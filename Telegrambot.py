import telegram
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

chat_token = "1671094125:AAGcJxhLg-HmGz-K4VRHWBT9xvl90ZwMjfE"


def start(update, context):
    """
    안녕하세요, intheshop에 알림을 등록해주셔서 감사합니다!
    update.message.reply_text('안녕하세요, intheshop에 알림을 등록해주셔서 감사합니다!' + '\n\n' + '알림 정보 등록 확인을 위해 /info 눌러주세요! 🧐' + '\n')
    # 동일한 사용자에게 응답 할 수 있도록 chat_id 가져 오기
    # 이 특정 메시지에 응답 할 수 있도록 메시지 ID 가져 오기
    """
    chat_id = update.message.chat.id
    msg_id = update.message.message_id
    update.message.reply_text(
        '안녕하세요, intheshop에 알림을 등록해주셔서 감사합니다!' + '\n\n' + '💌intheshop-push.shop💌 에서 등록한!' + '\n' + '연락처를 입력해주세요!(형식: 01012345678)' + '\n\n' + '등록한 정보가 다를 경우 알림을 보내드릴 수 없습니다ㅠ-ㅠ')


def get_info(update, context):
    """
    핸드폰 번호 확인!
    # update.message.reply_text('💌intheshop-push.shop💌 에서 등록한 연락처를 입력해주세요!')
    """
    telephone = update.message.text
    if telephone is not None:
        print(telephone)
        update.message.reply_text('감사합니다!' + '\n\n' + '최저가 딜이 등록되면 알림 드리겠습니다👌🏼')


updater = Updater(chat_token)
start_handler = CommandHandler('start', start)
updater.dispatcher.add_handler(start_handler)
info_handler = MessageHandler(Filters.text, get_info)
updater.dispatcher.add_handler(info_handler)
updater.start_polling(timeout=3, clean=True)
updater.idle()

# photo_handler = MessageHandler(Filters.photo, get_photo)
# updater.dispatcher.add_handler(photo_handler)
# file_handler = MessageHandler(Filters.document, get_file)
# updater.dispatcher.add_handler(file_handler)
