import csv

personal_info = [{'name': 'Маша', 'age': 25, 'job': 'Scientist'},
                 {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
                 {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'}]

with open('personal_info.csv', 'w', encoding='utf-8', newline='') as f:
    headers = list(personal_info[0].keys())
    writer = csv.DictWriter(f, headers, delimiter=';')
    writer.writeheader()
    writer.writerows(personal_info)
