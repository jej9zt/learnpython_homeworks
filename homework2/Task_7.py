dic = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую",
       "Есть минутка?": "Нет", "Какая погода?": "Холодно"}


def ask_user(dic):
    ask = input('Введите вопрос: ')
    if ask in dic:
        print(dic[ask])


while True:
    ask_user(dic)
