# x = print('Hello!')
# y = set()
#
# print(type(x))
# print(type(y))
#
# print(x)
# print(y)


# my_list = [1,2,3]
# my_list.append(4)
# print(my_list)
# my_list.clear()
# print(my_list)

# def print_greeting():
#     '''
#     Print a greeting
#     :return: None
#     '''
#     print("Hello World")
# print_greeting()
# help(print_greeting)

# def print_greeting_with_name(name = 'John'):
#     '''
#     :param name
#     :return: None
#     '''
#     print("Hello " + name + '!')
# print_greeting_with_name('John')
# help(print_greeting_with_name)

# def sum_of_two_numbers(a =0,b=0):
#     '''
#     Sum of two numbers
#     :param a: The first number
#     :param b: The second number
#     :return: Sum of a and b
#     '''
#     return a + b
# x = sum_of_two_numbers(21,1)
# print(x)
# help(sum_of_two_numbers)

# def is_hello_in_text(text):
#      return 'hello' in text.lower()
#
# print(is_hello_in_text("Say hello everyone!"))
# print(is_hello_in_text("Hello everyone!"))

# def greeting_depends_on_gender(name, gender):
#     if gender == "male":
#         print("Welcome " + name + "!")
#         return gender
#     elif gender == "female":
#         print("Welcome " + name + "! You are so nice!")
#         return gender
#     else:
#         print("Welcome " + name + "! I never seen the creature like you")
#         return gender
#
#
# returned_value = greeting_depends_on_gender("John", "male")
# returned_value = greeting_depends_on_gender("Ja", "cmale")

# Homework
# def cat_voice():
#     print("Meow!")
#
# def dog_voice():
#     print("Woof!")
#
# cat_voice()
# dog_voice()

# def cat_voice():
#     print("Meow!")
#
# def dog_voice():
#     print("Woof!")
#
# cat_voice()
# dog_voice()
# cat_voice()
# dog_voice()

# def get_voice():
#     voice = input("Enter your voice: ")
#     return voice + '!'
# print(get_voice())


def odd_numbers(a, b):
    result = []

    for num in range(a, b + 1):
        if num % 2 != 0:
            result.append(num)

    return result


print(odd_numbers(1, 10))


def odd_numbers_lc(a, b):
    return [num for num in range(a, b + 1) if num % 2 != 0]


print(odd_numbers_lc(1, 10))