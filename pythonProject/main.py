x = "камень"
y = "бумага"
z = "ножницы"

print(x,y,z)

play_again = bool(True)
while play_again:
    name1 = num1 = input("Введите имя ")
    name2 = num2 = input("Введите имя ")

    num1 = input("Выберите: камень, ножницы, бумага ")
    num2 = input("Выберите: камень, ножницы, бумага ")

    if num1 == "камень" and num2 == "ножницы":
        print(f"Побеждает {name1}")

    elif num1 == "камень" and num2 == "бумага":
        print(f"Побеждает {name2}")

    elif num1 == "камень" and num2 == "камень":
        print("Ничья")

    elif num1 == "ножницы" and num2 == "камень":
        print(f"Побеждает {name2}")

    elif num1 == "ножницы" and num2 == "ножницы":
        print("Ничья")

    elif num1 == "ножницы" and num2 == "бумага":
        print(f"Побеждает {name1}")

    elif num1 == "бумага" and num2 == "камень":
        print(f"Побеждает {name1}")

    elif num1 == "бумага" and num2 == "ножницы":
        print(f"Побеждает {name2}")

    elif num1 == "бумага" and num2 == "бумага":
        print("Ничья")

    else:
        print("Даже в это не способны играть. Дауны")
    play_again = input("Сыграть еще раз? (yes/no)")

    if play_again == "yes":
        play_again = True
    else:
        play_again = False
print("Надеемся, вам игра понравилась")