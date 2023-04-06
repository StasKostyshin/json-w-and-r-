import json
import time

########################################## Задание #####################################################
# Пользователь будет вводить название и стоимость каждой своей покупки за день, до тех пор пока не
# напишет 'стоп'. Ваша задача записать это в json файл в формате:
# {'название': 'яблоко',
# 'стоимость': '200'}
####### Задача № 2
# Прочитать файл из предыдущего задания и вывести стоимость всех покупок за день

def js():
    goods = []
    money = 0
    while True:
        named = input('Введите название товара: ').strip().title()
        if named == 'Стоп':
            break
        else:
            cash = input('Введите стоимость товара: ')
            if not cash.isdigit():
                print('Не корректно введено количество')
                return js()
            money += int(cash)
            data = {"Date": time.ctime(),"Название": named,"Стоимость": cash} # задаём данные как словарь
            goods.append(data)# вносим их в список
    return goods, money # Возвращаем список и сумму стоимости

goods, money = js()

with open('data_in.json', 'w', encoding='UTF-8') as file: # открываем файл на запись присвоив имя file
     json.dump(goods, file, indent=0, ensure_ascii=False) # Записываем объект (goods) в (file) как json

with open('data_in.json', 'r', encoding='utf-8') as file: # Читаем файл присвоив имя file
    goods_all = json.load(file) # Читаем весь файл
    print(goods_all)
    print('Общая стоимость за товары ',time.ctime(),"Составила : ", money, 'монет')


