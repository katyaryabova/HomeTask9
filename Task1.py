def arithmetic(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b

    elif operation == "*":
        return a * b

    elif operation == "/":
        return a / b

    else:
        print("Неизвестная операция")


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
operation = str(input("Введите знак операции:"))
print("result: ", arithmetic(a, b, operation))
