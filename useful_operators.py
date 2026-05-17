# for x in range(3, 10, 2):
#     print(x)
# print(range(5))
# print(list(range(5)))

# letter_index = 0
# my_string = 'adsfkje'
# for letter in my_string:
#     print(letter + ' is at index ' + str(letter_index))
#     letter_index = letter_index + 1


# my_string = 'adsfkje'
# for item in enumerate(my_string):
#     print(item)

# print('a' in 'Jack')
# print('2' in 'Jack')
# print(str(2) in 'Jack')

# letter_list = ['a', 'b', 'c']
# print('a' in letter_list)
# print( 1 in letter_list)

# print(min(1,3,56,777))
# print(max(1,22,35,1123,0))
#
# my_list = [1,3,65,78]
# print(min(my_list))
# print(max('Hello'))
# for letter in 'Hello':
#     print(ord(letter))

from random import shuffle
my_list = [1,3,54,4]
shuffle(my_list)
print(my_list)

from random import randint
print(randint(1,10))