questions = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую",
             "Есть минутка?": "Нет", "Какая погода?": "Холодно"}


def ask_user(questions):
    ask = input('Введите вопрос: ')
    answer = questions.get(ask)
    if answer:
        print(answer)


while True:
    ask_user(questions)
