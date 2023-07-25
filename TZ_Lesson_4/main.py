names = []
numbers = []
services = []

while True:
    admin = input('Введите тип: ')
    if admin == 'Имя':
        names.append(input('Введите имя: '))
        print(names)
    elif admin == 'Номер':
        numbers.append(input('Введите номер: '))
        print(numbers)
    elif admin == 'Услуга':
        services.append(input('Введите услугу: '))
        print(services)
    elif admin == 'Стоп':
        break
    else:
        print('End')