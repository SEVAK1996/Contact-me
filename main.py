from telegram.ext import Updater, CommandHandler
from coingecko_scanner import check_and_trade

TOKEN = '8180889972:AAE7Abf5TzOXkEDI8fBe4oKXrQbIdDl3QA0'  # Քո Telegram բոտի թոքենը

def start(update, context):
    update.message.reply_text("👋 Բարև, Սևակ։ Քո բոտը ակտիվ է։
Մուտք գործի /trade՝ գնի ստուգման համար։")

def trade(update, context):
    result = check_and_trade()
    update.message.reply_text(result)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("trade", trade))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()