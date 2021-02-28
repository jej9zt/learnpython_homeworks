import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import ephem
import re
import operator

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


def get_city(city_end_letter, cities_dict):
    try:
        return cities_dict[city_end_letter].pop()
    except KeyError:
        return None


def cities_game_core(city, user_data):
    cities_dict = user_data['cities_dict']
    cities_used = user_data['cities_used']
    try:
        if get_last_letter(cities_used[-1]) != city[0].upper():
            return f'Напиши город на букву {get_last_letter(cities_used[-1])}'
    except IndexError:
        pass
    if city in cities_used:
        return f'{city} уже использовался, напиши другой'
    try:
        cities_dict[city[0]].remove(city)
    except KeyError:
        return 'Я незнаю такого города, напиши другой'
    city_end_letter = get_last_letter(city)
    city_answer = get_city(city_end_letter, cities_dict)
    if city_answer:
        cities_used += (city, city_answer)
    else:
        return 'Ты победил, у меня больше нет вариантов!'
    return f'{city_answer}, ваш ход'


def create_cities_dict(cities_list):
    cities_dict = {}
    for city in cities_list:
        if re.match(fr'{city[0]}.*?', city):
            if cities_dict.get(city[0]):
                cities_dict[city[0]].add(city)
            else:
                cities_dict[city[0]] = {city}
    return cities_dict


def cities_game(update, context):
    if context.args:
        city = context.args[0].capitalize()
        if not context.user_data.get('cities_dict'):
            context.user_data['cities_used'] = []
            with open('goroda.txt', 'r') as f:
                context.user_data['cities_dict'] = create_cities_dict(
                    f.read().splitlines())
            update.message.reply_text(cities_game_core(city,
                                                       context.user_data))
        else:
            update.message.reply_text(cities_game_core(city,
                                                       context.user_data))


def get_sign(calc_items):
    math_signs = ['+', '-', '*', '/']
    for sign in math_signs:
        if calc_items.find(sign) >= 0:
            return sign


def calculate(calc_items_list, sign):
    math_operators = {'+': operator.add, '-': operator.sub,
                      '*': operator.mul, '/': operator.truediv}
    for item in calc_items_list:
        if not item.isdigit():
            return 'Что-то тут не так, напиши 2+2 например'
    a, b = calc_items_list
    try:
        return math_operators[sign](int(a), int(b))
    except ZeroDivisionError:
        return 'На ноль делить нельзя. Подели не на ноль'


def calc(update, context):
    if context.args:
        calc_items = ''.join(context.args)
        if len(calc_items) < 3:
            update.message.reply_text('Что-то тут не так, напиши 2+2 например')
        else:
            sign = get_sign(calc_items)
            calc_items_list = calc_items.split(sign)
            if len(calc_items_list) == 2:
                update.message.reply_text(calculate(calc_items_list, sign))


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
