import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import ephem
import re
from random import choice

logging.basicConfig(filename='bot.log', level=logging.INFO)

CITIES = range(1)


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


def full_moon(update, context):
    date = update.message.date
    next_full_moon = ephem.next_full_moon(date)
    update.message.reply_text(next_full_moon)


def word_count(update, context):
    message_list = update.message.text.split()
    if len(message_list) > 1:
        word_count_items = message_list[1:]
        word_list = []
        for word in word_count_items:
            if re.match(r'\b[A-Za-zА-Яа-я].*?\b', word):
                word_list.append(word)
        if len(word_list) > 0:
            word_counts = len(word_count_items)
            update.message.reply_text(f'{word_counts} слова.')


def get_last_letter(word):
    exclude_letters = ['Й', 'Ь', 'Ы', 'Ъ']
    word_end_letter = word[-1].upper()
    if word_end_letter in exclude_letters:
        return get_last_letter(word[:-1])
    return word_end_letter


def get_citi(citi_end_letter, cities_list):
    citi_answer_list = []
    for citi in cities_list:
        if re.match(rf'^{citi_end_letter}.*?', citi):
            citi_answer_list.append(citi)
    citi_answer = choice(citi_answer_list)
    if citi_answer:
        return citi_answer
    return None


def cities_game_core(citi, user_data):
    cities_list = user_data['cities_list']
    cities_used = user_data['cities_used']
    if citi in cities_list:
        if len(cities_used) == 0:
            cities_list.remove(citi)
            citi_end_letter = get_last_letter(citi)
            citi_answer = get_citi(citi_end_letter, cities_list)
            cities_list.remove(citi_answer)
            cities_used += (citi, citi_answer)
        elif (len(cities_used) > 0 and
              get_last_letter(cities_used[-1]) == citi[0].upper()):
            cities_list.remove(citi)
            citi_end_letter = get_last_letter(citi)
            citi_answer = get_citi(citi_end_letter, cities_list)
            if citi_answer:
                cities_list.remove(citi_answer)
                cities_used += (citi, citi_answer)
            else:
                return 'Ты победил, у меня больше нет вариантов!'
        elif len(cities_used) > 0:
            return f'Напиши город на букву {get_last_letter(cities_used[-1])}'
        return f'{citi_answer}, ваш ход'
    elif (citi not in cities_list and len(cities_used) > 0 and
          get_last_letter(cities_used[-1]) != citi[0].upper()):
        return f'Напиши город на букву {get_last_letter(cities_used[-1])}'
    elif citi in cities_used:
        return f'{citi} уже использовался, напиши другой'
    return 'Я незнаю такого города, напиши другой'


def cities_game(update, context):
    if context.args:
        citi = context.args[0]
        if not context.user_data.get('cities_list'):
            context.user_data['cities_used'] = []
            with open('goroda.txt', 'r') as f:
                context.user_data['cities_list'] = f.read().splitlines()
            update.message.reply_text(cities_game_core(citi,
                                                       context.user_data))
        else:
            update.message.reply_text(cities_game_core(citi,
                                                       context.user_data))


def get_sign(calc_items):
    math_signs = ['+', '-', '*', '/']
    for sign in math_signs:
        if calc_items.find(sign) >= 0:
            return sign


def calc(update, context):
    if context.args:
        calc_items = ''.join(context.args)
        if len(calc_items) < 3:
            update.message.reply_text('Что-то тут не так, напиши 2+2 например')
        else:
            sign = get_sign(calc_items)
            if sign == '+' and len(calc_items.split(sign)) == 2:
                a, b = calc_items.split(sign)
                answer = int(a) + int(b)
            elif sign == '-' and len(calc_items.split(sign)) == 2:
                a, b = calc_items.split(sign)
                answer = int(a) - int(b)
            elif sign == '*' and len(calc_items.split(sign)) == 2:
                a, b = calc_items.split(sign)
                answer = int(a) * int(b)
            elif sign == '/' and len(calc_items.split(sign)) == 2:
                a, b = calc_items.split(sign)
                answer = int(a) / int(b)
            update.message.reply_text(answer)


def main():
    bot = Updater(settings.bot_key, use_context=True)
    dp = bot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet))
    dp.add_handler(CommandHandler('next_full_moon', full_moon))
    dp.add_handler(CommandHandler('wordcount', word_count))
    dp.add_handler(CommandHandler('cities', cities_game))
    dp.add_handler(CommandHandler('calc', calc))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Bot starting')
    bot.start_polling()
    bot.idle()


if __name__ == '__main__':
    main()
