# st = 'H'
# print(st[0])
# st = 'Hello World'
# print(st)

# for i in range(len(st)):
#     print(st[i],end='')


# print()
# for el in st:
#     print(el,end='')

# st = 'Hello World'

# if st.startwich('H'):
#     print("String starts wich H")
# else:
#     print('String does start witch H')

# if st[0]=='H':
#     print("String starts wich H")

# st = "Hello world"

# st = "Hello World"

# s = st.upper()  # Convert to uppercase
# # s ='HELLO WORLD'  # Assign a new value to s

# print(st)
# print(s)

# st = "Hello World  "

# print(st)
# print(st.strip())  # Remove leading and trailing whitespace
# print(st.lstrip())  # Remove leading whitespace 

# ind = str.find(st, "o")  # Find the first occurrence of "o"
# print(ind)  # Output: 4

# print(st[6:]) # World  (from index 6 to the end)
# print(st[0:5]) # Hello (from index 0 to 4)
# print(st[0:5:2]) # Hlo (from index 0 to 4 with step 2)
# print(st[::2]) # Hlo ol (from index 0 to the end with step 2)

# arr= [1, 2, 3, 4, 5]
# print(arr[::2]) # [1, 3, 5] (from index 0 to the end with step 2)

# print(arr[:len(arr)]) # [1, 2, 3, 4, 5] (from index 0 to the end)

# st = "Разбивает строку на подстроки"
# print(st)

# arr = st.split(' ')
# print(arr) # разбивает от пробела до пробела

# print('----------------')

# str = " ".join(arr)
# print(str) # собирает розделённые части

# Задание 1
# Пользователь вводит с клавиатуры строку. Произве-
# дите поворот строк и полученный результат выведите
# на экран.

# st = input('Введите строку: ')
# st = st[::-1]
# print(st)

# Задание 2
# Пользователь вводит с клавиатуры строку. Посчи-
# тайте количество букв, цифр в строке. Выведите оба
# количества на экран.

# Задание 2
# Пользователь вводит с клавиатуры строку. Посчитайте количество букв, цифр в строке. Выведите оба количества на экран.

# st = input("Введите строку: ")
# numbers = 0
# letters = 0
# for i in st:
#     if i.isdigit():
#         numbers += 1
#     elif i.isalpha():
#         letters += 1
# print(f"Количество букв: {letters}, количество цифр: {numbers}")

# Задание 3
# Пользователь вводит с клавиатуры строку и символ
# для поиска. Посчитайте сколько раз в строке встречается
# искомый символ. Полученное число выведите на экран.

# Задание 3
# Пользователь вводит с клавиатуры строку и символ
# для поиска. Посчитайте сколько раз в строке встречается
# искомый символ. Полученное число выведите на экран.

# st = input("Введите строку: ")
# symbol = input("Введите символ: ")

# count = 0
# for i in st:
#     if i == symbol:
#         count += 1  
# print(f"Количество вхождений символа '{symbol}' в строке: {count}")

# human = ("Tom", 37, "Google", "software developer")

# name, age, company, position = human

# print(name)         # Tom
# print(age)          # 37
# print(position)     # software developer
# print(company)     # Google

# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
 
# users3 = users.intersection(users2) #ПЕРЕСЕЧЕНИЕ МНОЖЕСТВ
# print(users3)   # {"Bob"}

# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
 
# users3 = users.difference(users2) #РАЗНОСТЬ МНОЖЕСТВ
# print(users3)           # {"Tom", "Alice"}
# print(users - users2)   # {"Tom", "Alice"}

# dict = {"name": "John", "age": 30, "city": "New York"}
# print(dict)

# dict["country"] = "USA"
# print(dict)

# for key in dict:
#     print(key, dict[key])

# marks = {}.fromkeys(['математика', 'русский язык', 'физика'], 0)

# # Вывод: {'русский язык': 0, 'математика': 0, 'физика': 0}
# print(marks)
# marks['математика'] = 5
# marks['русский язык'] = 4
# marks['физика'] = 12
# for item in marks.items():
#     print(item)

# users_tuple = (
#     ("+111123455", "Tom"),
#     ("+384767557", "Bob"),
#     ("+958758767", "Alice")
# )
# users_dict = dict(users_tuple)
# print(users_dict)

# people = [
#     {"name": "Tom", "age": 39, "company": "SuperCorp", "languages": ["Python", "JavaScript"]},
#     {"name": "Bob", "age": 43, "company": "BigCorp", "languages": ["Python", "C++", "C#"]},
#     {"name": "Sam", "age": 28, "company": "LittleCorp", "languages": ["Python", "Java"]}
# ]


# people = [
#     {"name": "Tom", "age": 39, "company": "SuperCorp", "languages": ["Python", "JavaScript"]},
#     {"name": "Bob", "age": 43, "company": "BigCorp", "languages": ["Python", "C++", "C#"]},
#     {"name": "Sam", "age": 28, "company": "LittleCorp", "languages": ["Python", "Java"]}
# ]
# result = []
# for person in people:
#     new_person = {
#         "name": person["name"],
#         "Last language": person["languages"][-1]  # Get the last language from the list
#     }
#     result.append(new_person)

# print(result)
