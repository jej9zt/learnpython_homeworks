# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
# ???

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2
first_name_list = []
for i in range(len(students)):
    first_name_list.append(students[i]['first_name'])
first_name_set = set(first_name_list)
for value in first_name_set:
    print(f'{value}: ', first_name_list.count(value))

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
# ???

# Пример вывода:
# Самое частое имя среди учеников: Маша
first_name_list = []
for i in range(len(students)):
    first_name_list.append(students[i]['first_name'])
print('Самое частое имя среди учеников:',
      max(first_name_list, key=lambda first_name:
          first_name_list.count(first_name)))

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
# ???

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша
for i in range(len(school_students)):
    first_name_list = []
    for j in range(len(school_students[i])):
        first_name_list.append(school_students[i][j]['first_name'])
    print(f'Самое частое имя в классе {i+1}:',
          max(first_name_list, key=lambda first_name:
              first_name_list.count(first_name)))


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# ???

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.
for i in range(len(school)):
    male_count = 0
    female_count = 0
    class_name = school[i]['class']
    for j in range(len(school[i]['students'])):
        if is_male.get(school[i]['students'][j]['first_name']):
            male_count += 1
        else:
            female_count += 1
    print(f'В классе {class_name} {female_count} девочки '
          f'и {male_count} мальчика.')

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# ???

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
class_male_count = []
class_female_count = []
for i in range(len(school)):
    male_count = 0
    female_count = 0
    class_name = school[i]['class']
    for j in range(len(school[i]['students'])):
        if is_male.get(school[i]['students'][j]['first_name']):
            male_count += 1
        else:
            female_count += 1
    class_male_count.append((class_name, male_count))
    class_female_count.append((class_name, female_count))
class_male_count_max = max(class_male_count, key=lambda i: i[1])[0]
class_female_count_max = max(class_female_count, key=lambda i: i[1])[0]
print('Больше всего мальчиков в классе', class_male_count_max)
print('Больше всего девочек в классе', class_female_count_max)
