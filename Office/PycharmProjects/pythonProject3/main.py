clients = ['Sasha', 'Ivan', 'Wayne']
again = bool(True)
while again:
    command = input('Введите ')
    if command == 'Add':
        clients.append(input('Имя '))
        print(clients)
    elif command == 'Del':
        clients.remove(input('Имя '))
        print(clients)
    else:
        print('Fuck off')
    again = input('Это все? ')
    if again == 'Нет':
        again = True
    else: print('End')
    break