while True:
    x = int(input('Add value for х: '))
    y = int(input('Add value y: '))

    if x >= 1:
        print(x, '*', y, '=', x*y)
    if y >= 1:
        print(x, '-', y, '=', x-y)
    if x>=1:
        print(x, '+', y, '=', x + y)
    else:
        break