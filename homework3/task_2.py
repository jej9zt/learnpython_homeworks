# Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
with open('referat.txt', 'r') as f:
    my_file = f.read()
lengh_line = len(my_file)

# Подсчитайте количество слов в тексте
quantity_words = len(my_file.split())

# Замените точки в тексте на восклицательные знаки
# Сохраните результат в файл referat2.txt
with open('referat2.txt', 'w') as wf:
    wf.write(my_file.replace('.', '!'))
