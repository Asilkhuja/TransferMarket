a = float(input("Введи число"))
b = input("*-+/**")
c = float(input("Введи второе число"))
if b == "*":
    print(a*c)
elif b == "-":
    print(a-c)
elif b == "+":
    print(a+c)
elif b == "/":
    print(a/c)
elif b == "**":
    print(a**c)
else:
    print(error)
