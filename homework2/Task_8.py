questions = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую",
             "Есть минутка?": "Нет", "Какая погода?": "Холодно"}


def ask_user(questions):
    ask = input('Введите вопрос: ')
    if questions.get(ask):
        print(questions[ask])


while True:
    try:
        ask_user(questions)
    except KeyboardInterrupt:
        print('\nПока!')
        break
