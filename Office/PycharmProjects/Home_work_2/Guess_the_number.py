import random
x = random.randint(1, 51)
while True:
    number = int(input('Введите число от 1 до 50 ' ))
    print(number)
    if x == number:
        print('Ты угадал, умница!')
    elif x < number:
        print('Ты не угадал. Бери ниже ')
    elif x > number:
        print('Ты не угадал. Бери выше ')
    else:
        print('Лох')
    again = input("Попробуешь еще? ")

    if again == 'Да':
        again == True
    else:
        print('Ну и хрен с тобой!')
        break