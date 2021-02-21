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
    try:
        _, item = update.message.text.split()
        date = update.message.date
        try:
            planet = getattr(ephem, item)
            logging.info(planet)
            constellation = ephem.constellation(planet(date))
            update.message.reply_text(constellation)
        except AttributeError:
            planet_list = []
            for _x, _y, planet_name in ephem._libastro.builtin_planets():
                planet_list.append(planet_name)
            update.message.reply_text('Я знаю только эти планеты:\n{}'.
                                      format(planet_list))
    except ValueError:
        update.message.reply_text('Напиши /planet Planet_name')


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
