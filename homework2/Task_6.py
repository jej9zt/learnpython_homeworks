def hello_user():
    return input('Как дела?\n')


while hello_user() != 'Хорошо':
    hello_user()
