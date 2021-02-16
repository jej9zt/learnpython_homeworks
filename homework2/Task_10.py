import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import ephem

logging.basicConfig(filename='bot.log', level=logging.INFO)


def greet_user(update, context):
    update.message.reply_text('Привет!')


def talk_to_me(update, context):
    text = update.message.text
    logging.info(text)
    update.message.reply_text(text)


def planet(update, context):
    item = update.message.text.split()[1]
    date = update.message.date
    planet = getattr(ephem, item)
    logging.info(planet)
    constellation = ephem.constellation(planet(date))
    update.message.reply_text(constellation)


def main():
    bot = Updater(settings.bot_key, use_context=True)
    dp = bot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('Bot starting')
    bot.start_polling()
    bot.idle()


if __name__ == '__main__':
    main()
