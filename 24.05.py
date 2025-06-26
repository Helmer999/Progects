# class Car:    # Создание типа !!!!! 

#     def __init__(self,mod,col,pr): # конструктор класса - вызывается при создании каждого объекта !
#         self.model = mod
#         self.color = col
#         self.price = pr
# #----- интерфейс класса
#     def Move(self): #метод класса Car, интерфейс объекта Car
#         print('Move....')

#     def Print(self): #метод вывода 
#         print(f'Model:{self.model}\tColor:{self.color}\tPrice:{self.price}')

# #-------------------- использование обьектов класса Car

# obj1 = Car("Audi","Blue",15000)
# obj1.Move()
# obj1.Print()

# obj2 = Car("BMW","White",30000)
# obj2.Print()


# class Stadion:  # Создание типа

#     def __init__(self, name, date, country, city, size):  # Конструктор класса
#         self.name = name
#         self.date = date
#         self.country = country
#         self.city = city
#         self.size = size

# # ----- интерфейс
#     def Show(self):  # Вывод
#         print(f'Name: {self.name}\tDate: {self.date}\tCountry: {self.country}\tCity: {self.city}\tSize: {self.size}')
#     def GetName(self):
#         return self.name        
#     def GetDate(self):
#         return self.date
#     def GetCountry(self):
#         return self.country
#     def GetCity(self):
#         return self.city
#     def GetSize(self):
#         return self.size

# # -------------------- использование объектов класса 

# obj1 = Stadion('Camp Nou', '1957', 'Spain', 'Barcelona', 8000)
# obj1.Print()

# obj2 = Stadion('Wembley', '2007', 'England', 'London', 5000)
# obj2.Print()


