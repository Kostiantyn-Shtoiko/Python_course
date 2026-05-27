# class Car:
#
#     wheels_number = 4
#
#     def __init__(self, name, color, year, is_crashed):
#         self.name = name
#         self.color = color
#         self.year = year
#         self.is_crashed = is_crashed
#         print('Car is created')
#
#     def drive(self):
#         print(self.name + ' CAR IS DRIVING ')
#
#     def change_color(self, new_color):
#         self.color = new_color
#
#
# class Truck(Car):
#
#     wheels_number = 6
#
#     def __init__(self, name, color, year, is_crashed):
#         Car.__init__(self, name, color, year, is_crashed)
#         print('Truck is created')
#
#     def drive(self):
#         print(self.name + ' Truck IS DRIVING every day')
#
#     def load_cargo(self, weight):
#         print('Truck is loading ' + str(weight) + 'kg')
#
# man_truck = Truck('Man', 'Blue', '2020', True)
#
# print(man_truck.wheels_number)
# print(Car.wheels_number)
# man_truck.drive()
# man_truck.load_cargo(2343)


# Polymorphism

# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         raise NotImplementedError('Class successor must implement this method')
#
#
# class Dog(Animal):
#     def __init__(self,name):
#         self.name = name
#
#     def speak(self):
#         print(self.name + " says woof")
#
#
# class Cat(Animal):
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print(self.name + " says meow")
#
# class Mouse(Animal):
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print(self.name + " says pipipi")
#
# class Fish(Animal):
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print(self.name + " says nothing")
#
# spike = Dog('Spike')
# tom = Cat('Tom')
# jerry = Mouse('Jerry')
# freddy = Fish('Freddy')
#
# pet_list = [spike,tom,jerry,freddy]
#
# for pet in pet_list:
#     pet.speak()
#
# def pet_voice(pet):
#     pet.speak()
#
# pet_voice(tom)
#
# pet_voice(freddy)

# Homework

class GameCharacter:

    def __init__(self,name, health, level):
        self.name = name
        self.health = health
        self.level = level

    def speak(self):
        print('Hi, my name is '+ self.name)

class Villain(GameCharacter):

    def __init__(self,name, health, level):
        self.name = name
        self.health = health
        self.level = level

    def speak(self):
        print('Hi, my name is '+ self.name + ' and I will kill you')

    def kill(self, character):
        character.health = 0
        print("Bang-bang, now you're dead")


hero = GameCharacter("Arthur", 100, 5)
villain = Villain("Joker", 120, 7)

hero.speak()
villain.speak()

villain.kill(hero)
print(hero.health)