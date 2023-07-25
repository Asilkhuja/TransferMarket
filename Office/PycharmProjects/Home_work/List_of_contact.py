contacts = ['Mark', 'Paul', 'Shakura']
print(contacts)

again = bool(True)
while again:
    question = input('Что сделать? ')
    if question == 'Добавить':
        question_2 = input('Что добавить? ')
        contacts.append(question_2)
        print(contacts)

    elif question == 'Удалить':
        question_2 = input('Что удалить? ')
        contacts.remove(question_2)
        print(contacts)
    elif question == 'Заменить':
        question_2 = input('Что заменить?')
        zamena = contacts.index(question_2)
        new_contacts = input('Введите новый контакт ')
        contacts[zamena] = new_contacts
        print(contacts)
    else:
        print('Катись отсюда!')
    again = input('Что еще? ')

    if again == 'One more':
        again = True
    else:
        print('Хрен тебе!')
        break