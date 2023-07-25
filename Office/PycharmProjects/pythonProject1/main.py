a = int(input("Введите первое значение "))
b = input("Выберите оператор /*-+ ")
c = int(input("Введите второе значение "))

if b == '/':
    print(a/c)

elif b == '*':
    print(a*c)

elif b == '-':
    print(a-c)

elif b == '+':
    print(a+c)

else:
    print('Error')

