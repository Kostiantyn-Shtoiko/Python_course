# class Car:

#     wheels_number = 4
#
#     def __init__(self, name, color, year, is_crashed):
#         self.name = name
#         self.color = color
#         self.year = year
#         self.is_crashed = is_crashed
#
#
# VW_car = Car(name="VW 7 GTI", color="blue", year=7, is_crashed=False)
# print(VW_car.is_crashed)
# print(VW_car.name)
#
#
# audi_car = Car(name="Audi", color="blue", year=7, is_crashed=True)
# print(audi_car.name)
# print(audi_car.year)
# print(VW_car.wheels_number)
#
# number_of_wheels_of_3_cars = Car.wheels_number * 3
# print(number_of_wheels_of_3_cars)

# Homework

class BlokPost:

    def __init__(self, user_name, text, number_of_likes):
        self.user_name = user_name
        self.text = text
        self.number_of_likes = number_of_likes

post_1 = BlokPost(user_name="Kost212",text="More like",number_of_likes=1000)
post_2 = BlokPost(user_name="Julia",text="I funny",number_of_likes=3412)

post_2.number_of_likes = 0
print(post_1.number_of_likes)
print(post_2.number_of_likes)