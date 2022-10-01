print("Hello World!")
age = int(input("Сколько тебе лет?"))
name = input("Как тебя зовут?")
high = int(input("Какой твой рост?"))
print("Итак, вот твои данные:")
print("Имя:" + name )
print("Возраст:" + str(age))
print("Рост:" + str(high))

question = input("Хочешь что-то посчитать?(да/нет)")

error = "False"

if question == "да":
    a = float(input("Введите первое число:"))
    b = float(input("Введите второе число:"))
    c = input("Выберите действие(+, -, /, *):")
    if c == "+":
        k = a + b
    elif c == "-":
        k = a - b
    elif c == "/":
        if b == 0:
            print("На ноль делить нельзя!")
            error = "True"
        else:
            k = a / b
    elif c == "*":
        k = a * b
    if error == "False":
        print("Результат вычисления:" + str(k))
input()
