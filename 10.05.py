
# def Sum(a, b):
#     print(f"{a} + {b} = {a+b}")

# def Mult(a, b):
#     print(f"{a} x {b} = {a*b}")

# def Min(a, b):
#     print(f"{a} - {b} = {a-b}")

# def Div(a, b):
#     if b == 0:
#         print("Error: Division by zero is not allowed.")
#         return # Exit the function if b is zero
#     print(f"{a} / {b} = {a/b}")

# #------------------------------------
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# s = input("Input operation:")

# match s:
#     case '+':
#         Sum(a, b) # вызов функции
#     case '*':
#         Mult(a, b)
#     case '-':
#         Min(a, b)
#     case '/':
#         Div(a, b)
#     case _:
#         print("Invalid operation")

# Напишите функцию, которая принимает два числа в качестве параметра и отображает все четные числа между ними.

# def show_even(a, b):
#     for x in range(min(a, b) + 1, max(a, b)):
#         if x % 2 == 0:
#             print(x) 

# 1.  Написать функцию, которая возвращает куб числа.
# 2.  Написать функцию для нахождения наибольшего из двух чисел. 
# 3.  Написать функцию, которая возвращает истину, если передаваемое значение положительное и ложь, если отрицательное.
# 4.  Написать функцию, которая в зависимости от выбора пользователя вызывает функции сложения, произведения, вычитания, деления двух чисел (эти функции тоже нужно написать самостоятельно).

# Задание 3
# Напишите функцию, которая отображает пустой или заполненный квадрат из некоторого символа. Функция принимает в качестве параметров: длину стороны квадрата, символ и переменную логического типа: 

#    если она равна True, квадрат заполненный;
#    если False, квадрат пустой.


# def Square(length, symbol, filled):
#     if filled== True:
#         for i in range(length):
#             print(symbol * length)
#     else:
#         for i in range(length):
#             if i == 0 or i == length - 1:
#                 print(symbol * length)
#             else:
#                 print(symbol + ' ' * (length - 2) + symbol)


# Square(10, '*', True)
# Square(10, '*', False)

# 5.  Написать функцию, выводящую на экран прямоугольник с высотой N и шириной K.
# 6.  Написать функцию, которая проверяет, является ли переданное ей число простым? Число называется простым, если оно делится без остатка только на себя и на единицу.
# 7.  Написать функцию, вычисляющую факториал переданного ей числа.
# 8.  Написать функцию, которая принимает два параметра: основание степени и показатель степени, и вычисляет степень числа на основе полученных данных.
# 9.  Написать функцию, которая получает в качестве параметров 2 целых числа и возвращает сумму чисел из диапазона между ними.


def Sum(a,b):
    return a + b

def Min(a,b):
    return a-b

def MyPrint(str):
    print(f"Your text: {str}")

def Main(): # Главная функция программы, точка старта , вызывает другие функции
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    print(f"Сумма {a} и {b} = {Sum(a,b)}")
    print(f"Разность {a} и {b}= {Min(a,b)}")



Main() # Вызов главной функции
# Конец программы

def Sum(a, b):
    return a + b

def Mult(a, b):
    return a * b

def Min(a, b):
    return a - b

def Div(a, b):
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return # Exit the function if b is zero
    a / b

#------------------------------------
def Main():
    print(f"{a} + {b} = {Sum(a, b)}")
    print(f"{a} * {b} = {Mult(a, b)}")
    print(f"{a} - {b} = {Min(a, b)}")
    print(f"{a} / {b} = {Div(a,b)}")



a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
s = input("Input operation:")

match s:
    case '+':
        Sum(a, b) # вызов функции
    case '*':
        Mult(a, b)
    case '-':
        Min(a, b)
    case '/':
        Div(a, b)
    case _:
        print("Invalid operation")
Main()

def Sum(a,b):
    return a + b

def Min(a,b):
    return a-b

def MyPrint(str):
    print(f"Your text: {str}")

def Main(): # Главная функция программы, точка старта , вызывает другие функции
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    print(f"Сумма {a} и {b} = {Sum(a,b)}")
    print(f"Разность {a} и {b}= {Min(a,b)}")



Main() # Вызов главной функции
# Конец программы


def Sum(a, b):
    print(f"{a} + {b} = {a+b}")

def Mult(a, b):
    print(f"{a} x {b} = {a*b}")

def Min(a, b):
    print(f"{a} - {b} = {a-b}")

def Div(a, b):
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return # Exit the function if b is zero
    print(f"{a} / {b} = {a/b}")

def Calculate(a, b, operation):
    match operation:
        case '+':
            return Sum(a, b)
        case '*':
            return Mult(a, b)
        case '-':
            return Min(a, b)
        case '/':
            return Div(a, b)
        case _:
            print("Invalid operation")
#------------------------------------
def Main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    s = input("Input operation:")

    Calculate(a, b, s) # Вызов функции Calculate с параметрами a, b и s
#------------------------------------
Main() # Вызов главной функции
# Конец программы


