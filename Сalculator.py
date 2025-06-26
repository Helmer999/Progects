print('Kалькулятор (+, -, *, /, **)')

a = float(input('Введите первое число: '))
op = input('Операция: ')
b = float(input('Введите второе число: '))

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print('Ошибка: Деление на 0' if b == 0 else a / b)
elif op == '**':
    print(a ** b)
else:
    print('Неизвестная операция.')
