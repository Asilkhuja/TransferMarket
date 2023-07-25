while True:
    word = input('Введите слово: ')
    contrary = word[::-1]
    if word[::1] == contrary:
        print(f'{word} - слово палиндром')
    else:
        print(f'{word} - не является палиндромом')