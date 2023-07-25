school = {}


def add_info(**kwargs):
    print(kwargs)
    school[kwargs.get('name')] = {'age': kwargs.get('age'), 'weight': kwargs.get('weight'), 'hobby':kwargs.get('hobby') }
    print(school)

def remove_student():

    school.pop(name)
    print(school)

def get_student_info():
    print(school[name])

def update_student_info(**kwargs):
    school[kwargs.get('name')] = {'age': kwargs.get('age'), 'weight': kwargs.get('weight'), 'hobby':kwargs.get('hobby') }
    print(school)

def get_all_students():
    print(list(school.keys()))


def count_students():
    return len(list(school.keys()))



process = True
service = input('Hi! Please identify yourself: (admin) ')

while process:
    t = input('hello, boss! what do you want?(add/rem/inf/upd/all:   ')
    if t == 'add':
        name = input('Name of student: ')
        if name in school:
            print('this name has already added')
        else:
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

    elif t == 'inf':
        name = input('Name of student: ')
        get_student_info()

    elif t == 'upd':
        name = input('Name of student: ')
        age1 = int(input('new_age:   '))
        weight1 = int(input('new_weight:   '))
        hobby1 = input('new_hobby:   ')
        update_student_info(age=age1, weight=weight1, hobby=hobby1)

    elif t == 'all':
        get_all_students()

    elif t == 'count_all':
        print(count_students())

