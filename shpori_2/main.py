# x = {'name': 'Pasha', 'job': 'Saller'}
# print(x['name'])

# my_dict = {'names': ['Jordan', 'Pavel', 'Sasha'], 'users': 'Pasha', 'numbers': (99,80)}
# print(my_dict['names'][0])
# print(my_dict['names'][0][3])


# data = {'name': ['Jordan','Pavel'], 'age': (12,21), 'job':'programers'}
# print(data['job'][-1])


# x = input('Add name')
# y = {'names': x, 'job': 'programers'}
# print(y['names'])


# data = {'name': ['Jordan','Pavel'], 'age': (12,21), 'job':'programers'}
# print(data.values())
# print(data.keys())
# print(data.items())


# my_dict = {'name': 'Pavel', 'job': 'programers'}
# if 'name' in my_dict:
#     print('Да есть!')
# else:
#     print('Не понимаю о чем вы')



# my_dict = {'name': 'Pavel', 'job': 'programers'}
# if 'name' in my_dict.values():
#     print('Да есть!')
# else:
#     print('Не понимаю о чем вы')


# users = {}
# users['name'] = 'Pavel'
# users['job'] = 'Blowjob'
# print(users)


# cafees = {'Evos': {'Gorod': 'Tashkent', 'Filialov': 'Mnogo', 'Otkritiye': 2007}}
# cafees['Evos']['кухня'] = 'Fast Food'
# print(cafees)




# my_dict = {'name': 'Pavel', 'job': 'programers'}
# my_dict.popitem()
# print(my_dict)


#
# age = 21
# print({}.fromkeys('a', age))

#
# my2 = {'title':'Python for beginers'}
# print(my2.get('title'))

#
# my = dict(name= 'Jordan', age= 23, job= 'Developer')
# my2 = my.copy()
#my2 = my.get('name')
# print(my2)



# nums = [1,1,3,3,2,2,5]
# print(nums)
# nums1 = set(nums)
# print(nums1)



# prazdniki= {'Навруз': '21 marta', 'New Year': '31 december'}
# a = input('Which holyday? ')
# print(prazdniki.get(a))





# all_products = {'Весь склад':{}}
#
# admin = input('Что вы хотите сделать? ')
# if admin == 'fruits':
#     all_products['fruits'] =
# product_name = input('Введите название продукта: ')
# product_count = input('Введите количество: ')
# all_products['Весь склад'][product_name] = product_count
#
# all_products


# all_products = {'Весь склад':{}}
#
# while True:
#     admin =



#
# def say_hello():
#     print('Hello World')
#     return

# def create_list():
#     my_list = []
#     print(my_list)
#     return

# create_list()
# create_list()

#
# def create_list():
#     my_list = []
#     return  my_list
#
# create_list()
# print(create_list())

#
# def calc():
#     a = 5
#     b = 4
#
#     return a*b
#
# print(calc())



# def calc(a, b):
#     result = a*b
#
#     return result
# calc(3, 4)
# print(calc(3, 4))


# def spam2(a):
#     print(a+6)
#
# spam2(3)



#
# def calc(a, b = 2):
#
#     result = a * b
#     return result
#
# c = 5
#
# print(calc(c))



# def spam(a, b, c = 7):
#     print(a+b+c)
#
# spam(3,5)



# def calc(a, b):
#     result = a + b
#     return result
# calc(3, 5)
#
# print(calc(3,5))


# all_products = {'Sklad':{'name': 'Xleb', 'kol_va': 34}}
#
# def get_products(a):
#     print (all_products['Sklad'][a])
#
# get_products('name')



# def spam(*args):
#     return args
#
# print(spam(1,2,3, 'Hello'))


#
# def spam(*args):
#     result = args[0] + args[1]
#     return result
#
# a = int(input())
# b = int(input())
# print(spam(a, b))



# def spam(**kwargs):
#     return kwargs
#
# print(spam(nsme = 'my', age = 23))


# def spam(**kwargs):
#     for k,v in kwargs.items():
#         print(k,v)
#
# print(spam(name = 'my1', age = 26))


# def register():
#     pass


# def f(a):
#     if a %2 == 1:
#         print('nechet')
#     else:
#         print('chet')
#     return a
#
# k = bool(True)
# while k:
#     a = int(input())
#     print(f(a))
#     m = input('again? ')
#     if m == 'yes':
#         k = True
#     else:
#         k = False
#         print('Good luck')
#         break




# def calc(a, b):
#     result = a + b
#     return result
# calc(3, 5)
#
# print(calc(3,5))


# while True:
#     a = lambda x: x**3
#     k = int(input())
#     print(a(k))


# x = [1, 2, 3, '4']
# a = map(lambda d: d*2, x)
# print(list(a))


# x = ['Hello', 'Pavel']
# a = map(lambda d: d*3, x)
#
# print(list(a))



# num_1 = int(input('First numb: '))
#
# mat_oper = input('What to do? ')
#
# num_2 = int(input('Second numb: '))
#
#
# plus = lambda  x,y: x+y
#
# minus = lambda  x,y: x-y
#
# devision = lambda  x,y: x/y
#
# multiplying = lambda  x,y: x*y
#
#
# if mat_oper == '+':
#     print(plus(num_1, num_2))
#
# elif mat_oper == '-':
#     print(minus(num_1, num_2))
# elif mat_oper == '/':
#     print(devision(num_1, num_2))
# elif mat_oper == '*':
#     print(multiplying(num_1, num_2))
# else:
#     print('fuck off')



#while True:
    # word_1 = input('Type first the word: ')
    # word_2 = input('Type second word: ')
    #
    # a = lambda d, r: d+r
    # print(a(word_1, word_2))
    #

    # word = input('Type the word: ')
    # e = lambda t: t[:: -1]
    # print(e(word))



# x = [1, 2, -4, -4, -8, -7, 4, 15, 18, 19, 21, -98]
# a = filter(lambda c: c>0, x)
# print(list(a))




#print('Hello, World!')

#
# for i in range (1,5):
#    print('*' * i)



#spisok = ['hi', 2, 4.24, True, [1,2,3], (4,5,6), {'name', 'Pavel'}]




# x = 4
# print(f'это задача № {x}')
#


# while True:
#     a = int(input())
#     b = int(input())
#     if a > b:
#         print(f'{a}>{b}')
#     else:
#         print(f'{b}>{a}')


# def ctoto(k):
#     if k == k[:: -1]:
#         print('Палиндром')
#     else:
#         print('Не палиндром')
#




# def numb(a, b):
#     print(a**b)
#
#
# a = int(input())
# b = int(input())
#
# numb(a, b)


#
# users = {}
#
# name = input('Add name: ')
# value = input('Add value: ')
#
# users[name] = value
# print(users)


# nums = [12, 13, 39, 65, 339, 102, 225, 169, 676]
# for i in nums:
#     if i%13==0:
#         print(f'{i} делится на 13 без остатка')
#     else:
#         print('ПШЛНХ')






# while True:
#     a = lambda x: x**3
#     k = int(input())
#     print(a(k))


# nums = [5, 10, 3, 1, 8]
# for i in nums:
#     a = lambda i: i
#     print(a)


#
# nums = [5, 10, 15, 12, 4, 3, 8, 58, 1]
#
# a = map(lambda d:d*2, nums)
# print(list(a))


#
# def season(t):
#     if t in [1,2,12]:
#         print('Winter')
#     elif t in [3,4,5]:
#         print('Spring')
#     elif t in [6, 7, 8]:
#         print('Summer')
#     elif t in [9,10,11]:
#         print('Aotum')




#
# num = [5, 10, 3, 1, 6]
# sorted_numbers = sorted(num, key=lambda x: x)






# for i in range(1,101):
#     if '9' in str(i)[-1]:
#         print(i)
#     else:
#         pass




#
# class User:
#     name = 'Jordan'
#
# user1 = User()

#
# class Car:
#     type = 'Bugatti'
#     color = 'white'
#     max_speed = 300
#
# car1 = Car()
# print(car1.color, car1.max_speed)




# class Person:
#     name = 'Uguz'
#     age = 25
#     job = 'Huyesos'





# class A:
#     def __init__(self, model, color, year):
#         self.model = model
#         self.color = color
#         self.year = year
#     def change_color(self, new_color):
#         self.color = new_color
#
#
#
# nexia = A(model = 'Nexia', year = 2008, color= 'silver')
# print(nexia.model)
# print(nexia.color)
# nexia.change_color('Black')
# print(nexia.color)




# class Comment:
#     def __init__(self, username, text, likes):
#         self.username = username
#         self.text = text
#         self.likes = likes
#     def give(self):
#         print('Дайте коментарий')
#
# process = True
# while process:
#     comment_1 = Comment( username= input('Add your name:'), text= input('Add your text: '), likes= int(input('Put your like:')))
#     comment_1.give()
#     print(comment_1.username)
#     print(comment_1.text)
#     print(comment_1.likes)






#
# class A:
#     def __init__(self, model, color, year):
#         self.model = model
#         self.color = color
#         self.year = year
#     def change_color(self, new_color):
#         self.color = new_color
#
#
#
# nexia = A(model = 'Nexia', year = 2008, color= 'silver')
# print(nexia.model)
# print(nexia.color)
# color_to_change = input('На какой цвет менять? ')
# nexia.change_color(color_to_change)
# print(nexia.color)




#
# class BankAccaunt:
#     def __init__(self, username, balance):
#         self.username = username
#         self.balance = balance
#         return 'succes'
#
#     def deposit(self, add):
#         self.balance += add
#     def cash(self, money):
#         if money < self.balance:
#             self.balance += money
#         else:
#             return 'Not enough'
#
#     def my_balance(self):
#         return f'Your balance: {self.balance}'
#
#
# client = input('Add your name: ')
# account1 = BankAccaunt(client)
# while True:
#     admin = input('What do u want? ')
#     if admin.lower() == 'депозит':
#         dep = int(input('Сколько дене вы хотите вложить? '))
#         account1.deposit(dep)
#         print(account1.deposit(dep))
#     elif admin.lower() == 'обналичить':
#         cas = int(input('Сколько денег вы хотите снять? '))
#         account1.cash(cas)
#         print(account1.cash(cas))
#     elif admin.lower() == 'баланс':
#         print(account1.my_balance())
#     else:
#         print('What?')










# BancAccaunt_1 = BankAccaunt(username= input('Add your name: '), balance= int(input('Add your balance')))
# deposit_1 = int(input('Add value: '))
# BancAccaunt_1.deposit(deposit_1)
# print(BancAccaunt_1.balance)




#
# class User:
#     def __init__(self, username, number, mail, posts = []):
#         self.username = username
#         self.number = number
#         self.mail = mail
#         self.posts = posts
#
#     def
#
#


# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in a:
#     if i<5:
#         print(i)


# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
#
# c = [i for i in a if i in b]
# print(c)


# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
# result = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
# print(result)






#
# def spam(a,b, c = 7):
#     print(a+b+c)
#
# spam(3,5)


# all_products = {'Склад': {'name': 'Xleb', 'kol-vo': 34}}
#
# def get_products(a = 'name'):
#     print(all_products['Склад'][a])
#
# get_products()




#
# x = [1, 2, 3, '4']
#
# a = map(lambda d: d*2, x)
#
# print(list(a))


#
# x = [1, 3, 5, 7]
#
# a = map(lambda d: d/2, x)
#
# print(list(a))




#
# def decrement_list(nums):
#     o = list(map(lambda x: x-1, nums))
#     return  o
#
# print(decrement_list([1,2,3,4,5]))



# x = [1, 2, 3,'4']
# a = filter(lambda  d: d*2 == 4, x)
#
# print(list(a))



# l = [1, 2, 3, 4, 5, 6]
# a = list(filter(lambda x: x%2 == 0,l))
#
# print(a)


# x = [1, 2, -2, -4, -8, -7, 4, 14, 18, 20, -30]
# y = list(filter(lambda x: x >= 0, x))
# print(list(y))




























