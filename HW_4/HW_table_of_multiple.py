table = bool(True)
while True:
    number = int(input('Введите цифру: '))
    for i in range(1, 11):
        print(number, '*', i, '=', number * i)
    table = input('Повторить? ')
    if table == 'да':
        table = True
    else:
        break