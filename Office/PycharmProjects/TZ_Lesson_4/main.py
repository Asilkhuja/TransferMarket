names = []
nums = []
services = []

while True:
    admin = input('Что хотите сделать? ')
    if admin == 'Имя':
        new_name = input('Ваше имя: ')
        if new_name in names:
            print('Такое имя уже есть!')
            new_name1 = input('Введите имя заново: ')
            if new_name1 in names:
                print('Максимальное количество попыток!')
            else:
                names.append(new_name1)
                print('Ваше имя успешно добавлено!')
        else:
            names.append(new_name)
            print('Ваше имя успешно добавлено!')
    elif admin == 'Номер':
        new_num = input('Ваш номер: ')
        if new_num in nums:
            print('Такой номер уже есть!')
            new_num1 = input('Введите номер заново: ')
            if new_num1 in nums:
                print('Максимальное количество попыток!')
            else:
                nums.append(new_num1)
                print('Ваш номер успешно добавлен!')
        else:
            nums.append(new_num)
            print('Ваш номер успешно добавлен!')
    elif admin == 'Услуга':
        new_serv = input('Введите услугу: ')
        services.append(new_serv)
        print('Услуга успешно добавлена')
    else:
        print('Я вас не понял')