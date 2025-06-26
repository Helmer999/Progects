# people = [
#     {'name': 'Tom', 'age': 39, 'company': 'SuperCorp', 'languages': ['Python', 'JavaScript']},
#     {'name': 'Bob', 'age': 43, 'company': 'BigCorp', 'languages': ['Python', 'C++', 'C#']},
#     {'name': 'Sam', 'age': 28, 'company': 'LittleCorp', 'languages': ['Python', 'Java']}
# ]

# for person in people:
#     print(f"Name: {person['name']}")
#     print(f"Last language: {person['languages'][-1]}")

# print()


# Задание 1
# Пользователь вводит с клавиатуры название фрукта.
# Необходимо вывести на экран количество раз, сколько
# фрукт встречается в кортеже в качестве элемента.

# a = input(str('Введите название фрукта: '))

# fruits = [
#     {'name': 'banana' 'lemon' 'lecho', 'magazine': 'ATБ'},
#     {'name': 'aple' 'orange', 'magazine': 'METRO',},
#     {'name': 'kivi' 'aple',  'magazine': 'Tavria V',}
# ]

# tuple = ('orange', 'apple', 'apple', 'banana', 'organe')

# count = 0
# for b in tuple:
#     if b == a:
#         count+=1
# print(count)

# # ----симметрическая разность производится с помощью метода symmetric_difference() или с помощью операции ^. Она возвращает все элементы обоих множеств за исключением общих:
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
 
# users3 = users.symmetric_difference(users2)
# print(users3)   # {"Tom", "Alice", "Sam", "Kate"}
 
# users4 = users ^ users2
# print(users4)   # {"Tom", "Alice", "Sam", "Kate"}

# ---- Mодуль 8 — Kортежи, множества, словари
# ---- Задание 1, 2 и 3

# frukty = ('banana', 'apple', 'bananamango', 'mango', 'strawberry-banana', 'apple', 'banana')

# frukt = input('Zadanie 1\nVvedite nazvanie frukta: ').lower()

# kolichestvo = frukty.count(frukt)
# print(f'Frukt "{frukt}" vstrečaetsya točno {kolichestvo} raz(а).\n')

# kolichestvo1 = sum(1 for f in frukty if frukt in f)
# print(f'Frukt "{frukt}" vstrečaetsya kak čast’ stroki {kolichestvo1} raz(а).\n')

# avto = ('BMW', 'Audi', 'Toyota', 'BMW', 'Mercedes', 'BMW', 'Honda')

# zamena = input('Zadanie 3\nVvedite proizvoditel’, kotoryi nuzhno zamenit’: ')
# new = input('Vvedite novoe nazvanie: ')

# new_avto = tuple(new if a == zamena else a for a in avto)

# print('\nObnovlёнnyy kortezh proizvoditeley:')
# print(new_avto)

