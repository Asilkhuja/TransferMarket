import gspread
from oauth2client.service_account import ServiceAccountCredentials


#обязательные параметры
scope = ["https://spreadsheets.google.com/feeds",
         'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]


#авторизация ключей
creds = ServiceAccountCredentials.from_json_keyfile_name('credents.json', scope)

#Авторизация таблицы
client = gspread.authorize(creds)

######################################################################################################################

#Открытие таблицы
tablica = client.open('First_free_table')

#Открытие конкретного листа
konkretniy_list = tablica.worksheet('List1')
#
# #Получение всех данных из листа
# all_data = konkretniy_list.get_all_records()
#
# #Получение данных с конкретной строки
# row = konkretniy_list.row_values(1) #цифра отвечает за ряд
#
# #Получение данных с конкретной колонны
# colon = konkretniy_list.col_values(1) #цифра отвечает за колонну
#
#
# #Получание данных из одной ячейки
# cell = konkretniy_list.cell(1, 2).value #цифры отвечают за положение ячейки
#

#Обновление данных в конкретной ячейке
#konkretniy_list.update_cell(1, 1, 'Gandon') #цифры отвечают за положение ячейки

# #Добавление новых данных
# konkretniy_list.append_row(['Name', 'Age', 'Hobby'])
#
# #Удаление данных из определенного ряда
# konkretniy_list.delete_rows(2) #цифра отвечает за ряд
#
# #Поиск ячейки по элементу
# find = konkretniy_list.find('Gandon')
# print(find.col, find.row)



while True:
    admin = input('What do u wanna do? ')
    if admin == 'add':
        name = input('Name: ')
        age = int(input('Age: '))
        position = input('Position: ')
        konkretniy_list.append_row([name, age, position])
        print('Worker has been added')

    elif admin == 'delete':
        who_to_delete = input('Who to delete? ')
        list_of_workers = konkretniy_list.get_all_records()
        print(list_of_workers)
        if who_to_delete in list_of_workers[0].values():
            find = konkretniy_list.find(who_to_delete)
            konkretniy_list.delete_rows(find.row)
            print('Worker has been deleted')
        else:
            print('Incorrect name!')


























