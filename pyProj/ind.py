#!/usr/bin/env python3
# -*- coding: utf-8 -*-


shedule = []
while True:
    shedule.append({
     'название пункта назначения рейса': input('Пункт назначения? - '),
     'номер рейса': int(input('Номер рейса? - ')),
     'тип самолета': input('Тип самолета? - ')
    })
    if input('Напишите "д" чтобы продолжить ввод данных, "н" для завершения ввода.\n') == 'д':
        pass
    else:
        break
shedule = sorted(shedule, key=lambda row: row['номер рейса'])

for i in shedule:
    print(i)

destination = input('Рейс в какой город вас интересует?')
approved = []
for i in shedule:
    if i['название пункта назначения рейса'] == destination:
        approved.append(i)

for i in approved:
    print(i)
