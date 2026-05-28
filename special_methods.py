
# class Person:
#     def __init__(self,first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def __str__(self):
#         return f'{self.first_name} {self.last_name} '
#
#     def __len__(self):
#         return self.age
#
#     def __del__(self):
#         print('Person object deleted')
#
#     def __add__(self, other):
#         return self.age + other.age
#
#
# roma = Person("Roma", "White", 18)
# jack = Person("Jack", "Dsaw", 23)
#
# print(roma + jack)

# print(len([1,2,3,4,5]))
# print(roma)
# print(len(roma))
#
# del (roma)
#
# x = 5
# y = 3
#
# a = '5'
# b = '2'
# print(x + y)
# print(x.__add__(y))
# print(a + b)
# print(a.__add__(b))

# Homework

class Chain:

    def __init__(self, number_of_items):
        self.number_of_items = number_of_items

    def __str__(self):
         return f' Chain with {self.number_of_items} items'

    def __len__(self):
         return self.number_of_items

object1 = Chain(5)
print(object1)
print(len(object1))
object2 = Chain(51)
print(object2)
print(len(object2))