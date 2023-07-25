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





# class BankAccaunt:
#     def __init__(self, username, balance = 0):
#         self.username = username
#         self.balance = balance
#
#     def deposit(self, add):
#         self.balance += add
#         return 'succes'
#     def cash(self, money):
#         if money < self.balance:
#             self.balance -= money
#         else:
#             return 'Not enough'
#
#     def my_balance(self):
#         return f'Your balance: {self.balance}'
#
# client = input('Add your name: ')
# account1 = BankAccaunt(client)
# while True:
#     admin = input('What do u want? ')
#     if admin.lower() == 'депозит':
#         dep = int(input('Сколько дене вы хотите вложить? '))
#         print(account1.deposit(dep))
#     elif admin.lower() == 'обналичить':
#         cas = int(input('Сколько денег вы хотите снять? '))
#         print(account1.cash(cas))
#     elif admin.lower() == 'баланс':
#         print(account1.my_balance())
#     else:
#         print('What?')

















# class User:
#     def __init__(self, name, mail, age, phone_number, post):
#         self.name = name
#         self.mail = mail
#         self.age = age
#         self.phone_number = phone_number
#         self.post = post
#
#     def change_name(self, new_name):
#         if self.name != new_name:
#             self.name = new_name
#             return 'success'
#         else:
#             return 'This name has already added'
#
#     def change_number(self, new_number):
#         if self.phone_number != new_number:
#             self.phone_number = new_number
#             return 'success'
#         else:
#             return 'This phone number has already added'
#
#     def change_mail(self, new_mail):
#         if self.mail != new_mail:
#             self.mail = new_mail
#             return 'success'
#         else:
#             return 'This mail has already added'
#
#     def change_age(self, new_age):
#         if self.age != new_age:
#             self.age = new_age
#             return 'success'
#         else:
#             return 'This age has already added'
#
#     def update_post(self, new_post):
#         if self.post != new_post:
#             self.post = new_post
#             return 'success'
#         else:
#             return 'This post has already added'
#
#
#
#
# name_1 = input('Add your name:   ')
# User_1 = User(name=name_1, phone_number=int(input('Add your number: ')), mail=input('Add your mail: '),
#               age=int(input('Add your age: ')), post=input('Add your post: '))
# print(User_1.name)
# print(User_1.phone_number)
# print(User_1.age)
# print(User_1.mail)
# print(User_1.post)
#
#
# while True:
#     admin = input('What do u want? ')
#     if admin.lower() == 'change_num':
#         change_number_1 = int(input('Add new number: '))
#         print(User_1.change_number(change_number_1))
#
#     elif admin.lower() == 'change_name':
#         change_name_1 = input('Add new name: ')
#         print(User_1.change_name(change_name_1))
#
#     elif admin.lower() == 'change_mail':
#         change_mail_1 = input('Add new mail: ')
#         print(User_1.change_mail(change_mail_1))
#
#     elif admin.lower() == 'change_age':
#         change_age_1 = int(input('Add new age: '))
#         print(User_1.change_age(change_age_1))
#
#     elif admin.lower() == 'update_post':
#         update_post_1 = input('Update your post: ')
#         print(User_1.update_post(update_post_1))
#     elif admin.lower() == 'info':
#         print(User_1.name)
#         print(User_1.phone_number)
#         print(User_1.age)
#         print(User_1.mail)
#         print(User_1.post)
#     else:
#         print('what? ')










# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def change_name(self, new_name):
#         if self.name != new_name:
#             self.name = new_name
#             return 'success'
#         else:
#             return 'This name has already added'
#
#     def change_age(self, new_age):
#         if self.age != new_age:
#             self.age = new_age
#             return 'success'
#         else:
#             return 'This age has already added'
#
#
# person_1 = person(name=input('Enter name: '), age= int(input('Enter age: ')))
# person_2 = person(name=input('Enter name for second person: '), age= int(input('Enter age for second person: ')))
#
# print('name:', person_1.name, 'age:', person_1.age)
# print('name:', person_2.name, 'age:', person_2.age)
#
#
#
# while True:
#     admin = input('What do u want? ')
#     if admin.lower() == 'change_name_p1':
#         change_name_1 = input('Add new name: ')
#         print(person_1.change_name(change_name_1))
#
#     elif admin.lower() == 'change_name_p2':
#         change_name_1 = input('Add new name: ')
#         print(person_2.change_name(change_name_1))
#
#     elif admin.lower() == 'change_age_p1':
#         change_age_1 = int(input('Add new age: '))
#         print(person_1.change_age(change_age_1))
#
#     elif admin.lower() == 'change_age_p2':
#         change_age_1 = int(input('Add new age: '))
#         print(person_2.change_age(change_age_1))
#
#     elif admin.lower() == 'info':
#         print('name:', person_1.name, 'age:', person_1.age)
#         print('name:', person_2.name, 'age:', person_2.age)
#     else:
#         print("Sorry, I couldn't got u")




#
# class Class:
#     def __init__(self, name, age, GN):
#         self.name = name
#         self.age = age
#         self.GN = GN
#
#     def get_name(self):
#         return (self.name)
#
#     def get_age(self):
#         return (self.age)
#
#     def get_GN(self):
#         return (self.GN)
#
#     def set_name(self, new_name):
#         if self.name != new_name:
#             self.name = new_name
#             return 'success'
#         else:
#             return 'This name has already added'
#
#     def set_age(self, new_age):
#         if self.age != new_age:
#             self.age = new_age
#             return 'success'
#         else:
#             return 'This age has already added'
#
#     def set_GN(self, new_GN):
#         if self.GN != new_GN:
#             self.GN = new_GN
#             return 'success'
#         else:
#             return 'This group number has already added'
#
#
# student_1 = Class(name= 'Norman', age= 20, GN= '9A')
# student_2 = Class(name= 'Gary', age= 19, GN= '8Z')
# student_3 = Class(name= 'Uguz', age= 21, GN= '10B')
# student_4 = Class(name= 'Linda', age= 17, GN= '7M')
# student_5 = Class(name= 'Mia', age= 16, GN= '8K')
#
#
# print('name:', student_1.name, 'age:', student_1.age, 'group number:', student_1.GN)
# print('name:', student_2.name, 'age:', student_2.age, 'group number:', student_2.GN)
# print('name:', student_3.name, 'age:', student_3.age, 'group number:', student_3.GN)
# print('name:', student_4.name, 'age:', student_4.age, 'group number:', student_4.GN)
# print('name:', student_5.name, 'age:', student_5.age, 'group number:', student_5.GN)
#
#
#
# while True:
#     admin = int(input('Please select student from 1 till 5: '))
#     if admin == 1:
#         admin = input('What can I help u? (get:gn1, ga1, g_GN1 / update: sn1, sa1, s_GN1): ')
#         if admin.lower() == 'gn1':
#             print(student_1.get_name())
#
#         elif admin.lower() == 'ga1':
#             print(student_1.get_age())
#
#         elif admin.lower() == 'g_GN1':
#             print(student_1.get_GN())
#
#         elif admin.lower() == 'sn1':
#             change_name_1 = input('Enter new name: ')
#             print(student_1.set_name(change_name_1))
#
#         elif admin.lower() == 'sa1':
#             change_age_1 = int(input('Enter new age: '))
#             print(student_1.set_age(change_age_1))
#
#         elif admin.lower() == 's_GN1':
#             change_GN_1 = int(input('Update GN: '))
#             print(student_1.set_GN(change_GN_1))
#
#         elif admin.lower() == 'info':
#             print('name:', student_1.name, 'age:', student_1.age, 'group number:', student_1.GN)
#
#         else:
#             print('What?')
#
#     elif admin == 2:
#         admin = input('What can I help u? (get:gn2, ga2, g_GN2 / update: sn2, sa2, s_GN2): ')
#         if admin.lower() == 'gn2':
#             print(student_2.get_name())
#
#         elif admin.lower() == 'ga2':
#             print(student_2.get_age())
#
#         elif admin.lower() == 'g_GN2':
#             print(student_2.get_GN())
#
#         elif admin.lower() == 'sn2':
#             change_name_2 = input('Enter new name: ')
#             print(student_2.set_name(change_name_2))
#
#         elif admin.lower() == 'sa2':
#             change_age_2 = int(input('Enter new age: '))
#             print(student_2.set_age(change_age_2))
#
#         elif admin.lower() == 's_GN2':
#             change_GN_2 = int(input('Update GN: '))
#             print(student_2.set_GN(change_GN_2))
#
#         elif admin.lower() == 'info':
#             print('name:', student_2.name, 'age:', student_2.age, 'group number:', student_2.GN)
#
#         else:
#             print('What?')
#
#     elif admin == 3:
#         admin = input('What can I help u? (get:gn3, ga3, g_GN3 / update: sn3, sa3, s_GN3): ')
#         if admin.lower() == 'gn3':
#             print(student_3.get_name())
#
#         elif admin.lower() == 'ga3':
#             print(student_3.get_age())
#
#         elif admin.lower() == 'g_GN3':
#             print(student_3.get_GN())
#
#         elif admin.lower() == 'sn3':
#             change_name_3 = input('Enter new name: ')
#             print(student_3.set_name(change_name_3))
#
#         elif admin.lower() == 'sa3':
#             change_age_3 = int(input('Enter new age: '))
#             print(student_3.set_age(change_age_3))
#
#         elif admin.lower() == 's_GN3':
#             change_GN_3 = int(input('Update GN: '))
#             print(student_3.set_GN(change_GN_3))
#
#         elif admin.lower() == 'info':
#             print('name:', student_3.name, 'age:', student_3.age, 'group number:', student_3.GN)
#
#         else:
#             print('What?')
#
#     elif admin == 4:
#         admin = input('What can I help u? (get:gn4, ga1, g_GN4 / update: sn4, sa1, s_GN4): ')
#         if admin.lower() == 'gn4':
#             print(student_4.get_name())
#
#         elif admin.lower() == 'ga4':
#             print(student_4.get_age())
#
#         elif admin.lower() == 'g_GN4':
#             print(student_4.get_GN())
#
#         elif admin.lower() == 'sn4':
#             change_name_4 = input('Enter new name: ')
#             print(student_4.set_name(change_name_4))
#
#         elif admin.lower() == 'sa4':
#             change_age_4 = int(input('Enter new age: '))
#             print(student_4.set_age(change_age_4))
#
#         elif admin.lower() == 's_GN4':
#             change_GN_4 = int(input('Update GN: '))
#             print(student_4.set_GN(change_GN_4))
#
#         elif admin.lower() == 'info':
#             print('name:', student_4.name, 'age:', student_4.age, 'group number:', student_4.GN)
#
#         else:
#             print('What?')
#
#     elif admin == 5:
#         admin = input('What can I help u? (get:gn5, ga5, g_GN5 / update: sn5, sa5, s_GN5): ')
#         if admin.lower() == 'gn5':
#             print(student_5.get_name())
#
#         elif admin.lower() == 'ga5':
#             print(student_5.get_age())
#
#         elif admin.lower() == 'g_GN5':
#             print(student_5.get_GN())
#
#         elif admin.lower() == 'sn5':
#             change_name_5 = input('Enter new name: ')
#             print(student_5.set_name(change_name_5))
#
#         elif admin.lower() == 'sa5':
#             change_age_5 = int(input('Enter new age: '))
#             print(student_5.set_age(change_age_5))
#
#         elif admin.lower() == 's_GN5':
#             change_GN_5 = int(input('Update GN: '))
#             print(student_5.set_GN(change_GN_5))
#
#         elif admin.lower() == 'info':
#             print('name:', student_5.name, 'age:', student_5.age, 'group number:', student_5.GN)
#
#         else:
#             print('What?')
#     else:
#         print('Good by')
































# class Company:
#     def __init__(self, mechanics, engineers, designers):
#         self.mechanics = mechanics
#         self.engineers = engineers
#         self.designers = designers
#         class Project:
#             def __init__(self, p_mechanics, p_engineers, p_designers):
#                 self.p_mechanics = p_mechanics
#                 self.p_engineers = p_engineers
#                 self.p_designers = p_designers
#
#             def remaining_mechanics(self):
#                 if self.p_mechanics > 0:
#                     return self.mechanics
#                 else:
#                     print('Wrong')
#
#
#         Project_1 = Project(p_mechanics= int(input('Enter the total number of mechanics')),
#                     p_engineers= int(input('Enter the total number of engineers')),
#                     p_designers= int(input('Enter the total number of designers')))
#
#
#
#
# Company_1 = Company(mechanics= int(input('Enter the number of mechanics for project')),
#                 engineers= int(input('Enter the number of engineers for project')),
#                 designers= int(input('Enter the number of designers for project')))
#
#
#         admin = input('What do u want?')
#             if admin.lower() == 'remaining mech':
#                 print(Project_1.remaining_mechanics())




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





# class Animal:
#     def make_sound(selfs, s):
#         print(s)
#
# class Horse(Animal):
#     def dibi(self):
#         print('Лошадь встает на дыбы')
#
# mustang = Horse()
# mustang.make_sound('Igogo')
# mustang.dibi()


#
# class Car:
#     def __init__(self, type, wheels, engine, body):
#         self.type = type
#         self.wheels = wheels
#         self.engine = engine
#         self.body = body
#
#     def start(self):
#         return 'Turn on'
#
#     def stop(self):
#         return 'Off'
#
# class Kamaz(Car):
#     def __int__(self, type, wheels, engine, body):
#         self.type = type
#         self.wheels = wheels
#         self.engine = engine
#         self.body = body
#
#     def gruz(self):
#         return 'Везет большой груз!'
#
# car1 = Car(4, 1.5, 'small')
# kamaz1 = Kamaz(6,7, 'biiiiiig')
#
# print(car1.start())
# print(f'{kamaz1.type}KAMAZ: {kamaz1.start()}')
# print(kamaz1.gruz())




#
# class Fifa_22:
#     def __init__ (self, ball, player):
#         self.ball = ball
#         self.player = player
#
#     def shoot(self):
#         return 'Scored goal'
#
#     def concedered(self):
#         return 'Пропустил гол'
#
# class Fifa_23_mini:
#     def __init__ (self, ball, player):
#         self.ball = ball
#         self.player = player
#
#     def ijury(self):
#         return 'Got injury'
#
#
# fifa22 = Fifa_22(ball= 1, player= 11)
# fifa23 = Fifa_23_mini(ball=1, player=6)
#
# print(fifa22.shoot())
# print(fifa23.ijury())





#
# class Car:
#     def __init__(self, model, color, year):
#         self.model = model
#         self.year = year
#         self.color = color
#
# class Supercar(Car):
#     def __init__(self, model, color, year, sponsor):
#         super().__init__(model, color, year)
#         self.sponsor =sponsor
#
# spark = Car('Chevrolet', 'White', 2020)
# petronas = Supercar('MB', 'Black', 2021, 'AMG')
#
# print(petronas.year)



#
# class French:
#     def wee_wee(self):
#         return 'Wee wee'
#
#
# class English:
#
#     def yes_yes(self):
#         return 'Yes yes'
#
# class Russian(French, English):
#     def da_da(self):
#         return 'da da'
#
#
# daughter = Russian()
# print(daughter.da_da())
# print(daughter.wee_wee())
# print(daughter.yes_yes())



#
# class Shape:
#     @classmethod
#     def create(cls, shape_type):
#         if shape_type == 'circle':
#             return 'Krug'
#         elif shape_type == 'triangle':
#             return 'treugolnik'
#         elif shape_type == 'square':
#             return 'kvadrat'
#
# print(Shape.create('circle'))


#
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height\
#
#     @property
#     def area(self):
#         return self.width * self.height
#
# rectangle = Rectangle(4, 5)
# print(rectangle.area)
# rectangle.width = 6
# print(rectangle.area)



#
# class Worker:
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position
#
#
# class HR(Worker):
#
#     def __init__(self, name, position, password):
#         super().__init__(name, position)
#         self.password = password
#
#     def show_info(self, worker):
#         return worker.position
#
# worker_1 = Worker('Aleks', 'Manager')
# hr1 = HR('Mich', 'HR', 123)
#
# worker_name = input('Add name: ')
# if worker_name == worker_1.name:
#     print('Hello')
#
# else:
#     password = int(input('Parol'))
#     if password == hr1.password:
#         action = input('What do u wanna do?')
#         if action == 'position':
#             who = input('whose position do u wanna know?')
#             if who == worker_1.name:
#                 print(hr1.show_info(worker_1))
#
#             else:
#                 print('This worker is not here')
#




# class Player:
#     def __init__(self, speed, shoot, paass, dribling):
#         self.speed = speed
#         self.shoot = shoot
#         self.paass = paass
#         self.dribling = dribling
#
#
#
#
# class Striker:
#     def __init__(self, speed, shoot, paass, dribling, goals):
#         super().__init__(self, speed, shoot, paass, dribling)
#         self.goal = goals
#
#
# class Difender:
#     def __init__(self, speed, shoot, paass, dribling, diffence):
#         super().__init__(self, speed, shoot, paass, dribling)
#         self.diffence = diffence
#
#     def diffence(self):
#         return 'Отобрал мяч'
#
# class Midfilde:
#     def __init__(self, speed, shoot, paass, dribling, assistence):
#         super().__init__(self, speed, shoot, paass, dribling)
#         self.assistence = assistence
#
# class Goalkeeper:
#     def __init__(self, speed, shoot, paass, dribling, saves):
#         super().__init__(self, speed, shoot, paass, dribling)
#         self.saves = saves






# Домашнее задание:
#
# 1. Создайте класс `Shape` (Фигура), у
# которого есть метод `area()` (площадь) и метод `perimeter()` (периметр).
# Оставьте эти методы без реализации.
# - Создайте два подкласса класса `Shape`:
#
# -`Rectangle` (Прямоугольник), который принимает два аргумента `length` (длина) и
# `width` (ширина) при создании экземпляра класса. Реализуйте методы `area()` и
# `perimeter()` для расчета площади и периметра прямоугольника.
#
# -`Circle` (Круг), который принимает один аргумент `radius` (радиус) при создании
# экземпляра класса. Реализуйте методы `area()` и `perimeter()` для расчета
# площади и длины окружности круга.
#
# - Создайте объекты `Rectangle` и `Circle`,
# передавая необходимые значения при их создании.
#
# - Выведите на экран площадь и периметр
# прямоугольника и круга, используя соответствующие методы.

import math
class shape:
    def area(self):
        pass
    def perimeter(self):
        pass
class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    @property
    def area(self):
        return self.width * self.length
    def perimeter(self):
        return (self.width + self.length) * 2
class circle(shape):
    def __init__(self, radius):
        self.radius = radius
    @property
    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


process = True
while process:
    admin = input('choose shape:  ')
    if admin.lower() == 'rect':
        a = int(input('length:   '))
        b = int(input('width:   '))
        rec = rectangle(a, b)
        print(f'rectangle area =', rec.area)
        print(f'rectangle perimeter =', rec.perimeter())
    elif admin.lower() == 'cir':
        r = int(input('radius:   '))
        cir = circle(r)
        print(f'circle area =', cir.area)
        print(f'circle perimeter =', cir.perimeter())
    elif admin.lower() == 'stop':
        process = False
        break


















































