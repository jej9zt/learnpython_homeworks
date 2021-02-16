def get_status(age):
    if age < 7:
        status = 'Вы учитесь в детском саду.'
    elif 7 <= age < 18:
        status = 'Вы учитесь в школе.'
    elif 18 <= age < 22:
        status = 'Вы учитесь в ВУЗе.'
    elif age >= 22:
        status = 'Вы работаете.'
    return status


age = int(input('Введите свой возраст: '))
print(get_status(age))
