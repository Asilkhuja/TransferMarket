k = 'k - камень'
b = 'b - бумага'
n = 'n - ножницы'

print(k, n, b)

play_again = bool(True)
while play_again:
    name1 = input('first player: ')
    name2 = input('second player: ')

    num1 = input('Выберите: k, n, b ')
    num2 = input('Выберите: k, n, b ')

    if num1 == 'k' and num2 == 'n':
            print(f'Побеждает {name1}')

    elif num1 == 'k' and num2 == 'b':
            print(f'Побеждает {name1}')

    elif num1 == 'k' and num2 == 'k':
            print('Ничья')

    elif num1 == 'n'and num2 == 'k':
            print(f'Побеждает {name2}')

    elif num1 == 'n' and num2 == 'n':
            print('Ничья')

    elif num1 == 'n' and num2 == 'b':
            print(f'Побеждает {name1}')

    elif num1 == 'b' and num2 == 'k':
            print(f'Побеждает {name2}')

    elif num1 == 'b' and num2 == 'n':
            print(f'Побеждает {name2}')

    elif num1 == 'b' and num2 == 'b':
            print('Ничья')

    else:
            print('вам двоим нельзя играть в эту игру')
    play_again = input('Сыграть еще раз? (yes/no): ')

    if play_again == 'yes':
        play_again = True
    else:
        play_again = False
print('надеемся, вам игра понравилась')
