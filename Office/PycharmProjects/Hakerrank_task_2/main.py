# while True:
#     x = int(input('Введите значение для х: '))
#     y = int(input('Введите значение для y: '))
#
#     if x >= 1:
#         print(x, '*', y, '=', x*y)
#     if y >= 1:
#         print(x, '-', y, '=', x-y)
#     if x>=1:
#         print(x, '+', y, '=', x + y)
#     else:
#         break


if __name__ == '__main__':
    n = int(input().strip())
    if n %2:
        print('Not Weird')
    elif n in range(6,21):
        print('Weird')