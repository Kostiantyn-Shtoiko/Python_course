# class Car:
#
#     wheels_number = 4
#
#     def __init__(self, name, color, year, is_crashed):
#         self.name = name
#         self.color = color
#         self.year = year
#         self.is_crashed = is_crashed
#
#     def drive(self):
#         print(self.name + ' CAR IS DRIVING ')
#
#     def change_color(self, new_color):
#         self.color = new_color
#
# opel_car = Car('opel', 'red', 2019, True)
# mazda_car = Car('mazda', 'red', 2019, True)
# opel_car.drive()
# mazda_car.drive()
# print(opel_car.wheels_number)
# print(opel_car.color)
# mazda_car.change_color('blue')
# print(mazda_car.color)
# import math
#
#
# class Circle:
#     pi = 3.14159
#
#     def __init__(self, radius = 1):
#         self.radius = radius
#
#     def get_area(self):
#         return math.pi * (self.radius ** 2 )
#
#     def get_circumference(self):
#         return 2 * math.pi * self.radius
#
# circle_1 = Circle()
# print(circle_1.get_area())
# print(circle_1.get_circumference())
#
# circle_2 = Circle(4)
# print(circle_2.get_area())
# print(circle_2.get_circumference())

# Homework

class BankAccount:

    balance = 0

    def __init__(self, client_id, client_first_name, client_last_name,balance):
        self.client_id = client_id
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        self.balance = balance

    def add (self, amount):
        self.balance += amount
    def withdraw (self, amount):
        self.balance -= amount

account = BankAccount("221", "Yolo", "Das", 100)
account_1 = BankAccount("232", "Daq", "DFD", 762)
account.add(1222)
print(account.balance)

account_1.withdraw(5000)
print(account_1.balance)