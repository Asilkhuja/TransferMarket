hotel = {'all_rooms': ('a1', 'a2', 'a3', 'a4'),
         'free_rooms': ['a1', 'a2', 'a3', 'a4'],
         'busy_rooms': {}}

def all_rooms():
    print(hotel['all_rooms'])
#    return all_rooms()
def free_rooms():
    a = print(hotel['free_rooms'])
def busy_rooms():
    a = print(hotel['busy_rooms'])
def reg_guest():

    r = print('We have: ', hotel['free_rooms'])

#    print('We have: ', hotel['free_rooms'])
    room_number = input('choose room number: ')
    guest_name = input('typing name: ')

    hotel['busy_rooms'][room_number] = guest_name
    if room_number in hotel['free_rooms']:
        hotel['free_rooms'].remove(input('Repeat the selection of the room: '))
        print(hotel)
    return r



def del_guest():
    d = print('Would you like to turn off your room? ')
    room_number = input('Write your room number: ')
    hotel['busy_rooms'].pop(room_number)
    hotel['free_rooms'].append(room_number)
    print(hotel)
    return d


process = True
service = input('Hi! Please identify yourself: (admin) ')

while process:
        t = input('hello, boss! what do you want?   ')

        if t == 'all':
            all_rooms()
        elif t == 'free':
            free_rooms()
        elif t == 'busy':
            busy_rooms()
        elif t == 'reg':
            reg_guest()
        elif t == 'del':
            del_guest()