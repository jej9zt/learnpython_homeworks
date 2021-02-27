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
from collections import Counter

cnt = Counter()
for idx, _ in enumerate(students):
    cnt[students[idx]['first_name']] += 1
for name, quantity in cnt.items():
    print(f'{name}: ', quantity)

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
cnt = Counter()
for idx, _ in enumerate(students):
    cnt[students[idx]['first_name']] += 1
print('Самое частое имя среди учеников:', cnt.most_common(1)[0][0])


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
for i, _ in enumerate(school_students):
    cnt = Counter()
    for j, _ in enumerate(school_students[i]):
        cnt[school_students[i][j]['first_name']] += 1
    print(f'Самое частое имя в классе {i+1}:', cnt.most_common(1)[0][0])



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
for i, _ in enumerate(school):
    cnt = Counter()
    class_name = school[i]['class']
    for j, _ in enumerate(school[i]['students']):
        if is_male.get(school[i]['students'][j]['first_name']):
            cnt['male'] += 1
        else:
            cnt['female'] += 1
    print(f"В классе {class_name} {cnt['female']} девочки "
          f"и {cnt['male']} мальчика.")

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
male_cnt = Counter()
female_cnt = Counter()
for i, _ in enumerate(school):
    class_name = school[i]['class']
    for j, _ in enumerate(school[i]['students']):
        if is_male.get(school[i]['students'][j]['first_name']):
            male_cnt[class_name] += 1
        else:
            female_cnt[class_name] += 1
print('Больше всего мальчиков в классе', male_cnt.most_common(1)[0][0])
print('Больше всего девочек в классе', female_cnt.most_common(1)[0][0])
