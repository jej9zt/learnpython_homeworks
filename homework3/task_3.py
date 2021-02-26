import csv

personal_info = [{'name': 'Маша', 'age': 25, 'job': 'Scientist'},
                 {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
                 {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'}]

with open('personal_info.csv', 'w', encoding='utf-8', newline='') as f:
    headers = []
    for header in personal_info[0].keys():
        headers.append(header)
    writer = csv.DictWriter(f, headers, delimiter=';')
    writer.writeheader()
    for user_info in personal_info:
        writer.writerow(user_info)
