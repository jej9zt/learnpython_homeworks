questions = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую",
             "Есть минутка?": "Нет", "Какая погода?": "Холодно"}


def ask_user(questions):
    ask = input('Введите вопрос: ')
    if questions.get(ask):
        print(questions[ask])


while True:
    ask_user(questions)
