number = input('Введите число от 1 до 50 ')
import random
x = random.randint(1, 51)
again = bool(True)
while again:
    if x == number:
        print('Вы угадали')
    else:
        print('Вы не угадали')
    again = input("Попробуете еще? ")
    if again == x:
        again = True
    else:
        print('Лох')
        break
