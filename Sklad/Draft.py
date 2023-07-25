school = {}


def add_info(**kwargs):
    print(kwargs)
    school[kwargs.get('name')] = {'age': kwargs.get('age'), 'weight': kwargs.get('weight'),
                                  'hobby': kwargs.get('hobby')}
    print(school)


def remove_student():
    school.pop(name)
    print(school)


def get_student_info():
    print(school[name])


def update_student_info(**kwargs):
    school[kwargs.get('name')] = {'age': kwargs.get('age'), 'weight': kwargs.get('weight'),
                                  'hobby': kwargs.get('hobby')}
    print(school)


def get_all_students():
    print(school.keys())


def count_students():
    print(school.keys())


process = True
service = input('Hi! Please identify yourself: (admin) ')

while process:
    t = input('hello, boss! what do you want?(add/rem/ginf/upd/all:   ')
    if t == 'add':
        name = input('Name of student: ')
        if name in school:
            print('wsdfghjkl')
        age = int(input('age:   '))
        weight = int(input('weight:   '))
        hobby = input('hobby:   ')
        add_info(name=name, age=age, weight=weight, hobby=hobby)

    elif t == 'rem':
        name = input('Name of student: ')
        if name not in school:
            print('You have entered wrong name')

        else:
            remove_student()

    elif t == 'ginf':
        name = input('Name of student: ')
        get_student_info()

    elif t == 'upd':
        name = input('Name of student: ')
        age1 = int(input('new_age:   '))
        weight1 = int(input('new_weight:   '))
        hobby1 = input('new_hobby:   ')
        update_student_info(age=age1, weight=weight1, hobby=hobby1)

    elif t == 'allstdnts':
        get_all_students()

    elif t == 'count_all':

        count_students()