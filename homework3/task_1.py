from datetime import datetime, timedelta

# Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
today = datetime.today()
yesterday = today - timedelta(days=1)
early_30_day = today - timedelta(days=30)

print(today.strftime('%d/%m/%Y'))
print(yesterday.strftime('%d/%m/%Y'))
print(early_30_day.strftime('%d/%m/%Y'))

# Превратите строку "01/01/25 12:10:03.234567" в объект datetime
datetime_string = '01/01/25 12:10:03.234567'
date_dt = datetime.strptime(datetime_string, '%d/%m/%y %H:%M:%S.%f')
