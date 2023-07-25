while True:
    x = bool(True)
    number = int(input('напиши число: '))
    if (number % 2) == 1:
       print ('Weird')
    elif (number > 1 and number < 5 ):
       print( 'Not weird ')
    elif (number > 5 and number < 21):
       print ('Weird')
    else:
       print ('not Weird')
