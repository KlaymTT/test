a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = input("Знак: ")
if c == "+":
    print("Результат:",a+b)
elif c == "/" and b ==0:
    print("Результат: 0")
elif c == "-":
    print("Результат:",a-b)
elif c == "/":
    print("Результат:",a/b)
elif c == "*":
    print("Результат:",a*b)
else:
    print("Error")