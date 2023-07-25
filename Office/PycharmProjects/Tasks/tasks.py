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