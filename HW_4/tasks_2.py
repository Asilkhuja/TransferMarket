#bottles = bool(True)
#while bottles:
#    small_bottle = int(input('Enter number of small bottles: '))
#    big_bottle = int(input('Enter number of big bottles: '))
#    pay_for_small_bottle = float(small_bottle*0.1)
#    pay_for_big_bottle = float(big_bottle*0.25)
#    total_of_bottles = pay_for_small_bottle+pay_for_big_bottle
#
#    pay_1 = round(pay_for_small_bottle, 2)
#    pay_2 = round(pay_for_big_bottle, 2)
#    total = round(total_of_bottles, 2)
#
#    print(f'cash for small bottles: $ {pay_1}')
#    print(f'cash for big bottles: $ {pay_2}')
#    print(f'total cash: {total}')
#
#    command = input('Again? ')
#    if command == 'yes':
#        bottles = True
#    else:
#        print('Good luck')






#count = bool(True)
#while count:
#    bill = int(input('Введите сумму заказа: '))
#    tips = float(bill * 0.18)
#    taxes = float(bill * 0.15)
#    sum = bill + taxes + tips
#
#    tips_1 = round(tips, 2)
#    taxes_1 = round(taxes, 2)
#    b = round(sum, 2)
#
#    print(f'Чаевые = {tips_1}$')
#    print(f'Налоги = {taxes_1}$')
#    print(f'Итого = {b}$')
#
#    text = input('Повторить расчет?')
#    if text == 'да':
#        count = True
#    else:
#        count = False
#print('End')





#math = bool(True)
#while math:
#    n = int(input('Enter number: '))
#    sum = (n*(n+1))/2
#    print(sum)
#    a = input('Again? ')
#    if a == 'yes':
#        math = True
#    else:
#        print('End')





#package = bool(True)
#while package:
#    souvenier = int(input('Enter number of souveniers: '))
#    trinket = int(input('Enter number of trinkets: '))
#
#    mass_of_souv = float(souvenier*0.075)
#    mass_of_trinket = float(trinket*0.112)
#    total_package_weight = mass_of_souv + mass_of_trinket
#
#    mass_1 = round(mass_of_souv, 2)
#    mass_2 = round(mass_of_trinket, 2)
#    total = round(total_package_weight, 2)
#
#    print(f'Mass of souveniers are: {mass_1} kg')
#    print(f'Mass of trinkets are: {mass_2} kg')
#    print(f'Total package weight is: {total} kg')
#
#    a = input('Again? ')
#    if a == 'yes':
#        package = True
#    else:
#        print('Have a nice shopping!')