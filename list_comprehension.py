from List import new_list

# greeting = 'hello!'
# letter_list = []
# for letter in greeting:
#     letter_list.append(letter)
# print(letter_list)

# letter_list = [letter for letter in greeting]
# print(letter_list)
#
# number_list = [number for number in '0123456789']
# print(number_list)
#
# number_list_1 = [num for num in range(0, 10)]
# print(number_list_1)
#
# number_list_2 = [num ** 2 for num in range(0, 10)]
# print(number_list_2)
#
# number_list_3 = [((num - 3) / 2) ** 2 for num in range(0, 10)]
# print(number_list_3)

# number_list = [6, 21, -12, 234, -1, 676, 1, 22222, -7865]
# new_list_1 = [number for number in number_list if number > 0]
# print(new_list_1)

# Homework
# greetings = ['hello', 'hi', 'hey', 'hola']
# second_letters = [word[1] for word in greetings]
#
# print(second_letters)
#
# greetings = ['hello', 'hi', 'hey', 'hola']
# second_letters = []
# for word in greetings:
#     second_letters.append(word[1])
#
# print(second_letters)

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
num = [ num for num in digits if num % 2 == 1]
print(num)


digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
num = []
for d in digits:
    if d % 2 == 1:
        num.append(d)

print(num)