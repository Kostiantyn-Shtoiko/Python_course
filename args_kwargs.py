# def ten_percent_of_product(x, y,z):
#     return (x * y * z) * 0.1
#
# print(ten_percent_of_product(10, 20, 4))

# def ten_percent_of_product_with_args(*args):
#     product = 1
#     for number in args:
#         product = product * number
#     return product * 0.1
#
# print(ten_percent_of_product_with_args(12, 20, 4,1))

# def percent_of_product_with_args(percent, *args):
#     product = 1
#     for number in args:
#         product = product * number
#     return product / 100 * percent
#
# print(percent_of_product_with_args(10,12, 20, 4,1))

# def func_with_kwargs(**kwargs):
#     print(kwargs)
#
# func_with_kwargs(first = 1, second = 2, third = 3)

# def hello_with_kwargs(**kwargs):
#     if 'name' in kwargs:
#         print('Hello! Nice to meet you, {}'.format(kwargs['name']))
#     else:
#         print('Hello! What is your name?')
#
# hello_with_kwargs(gender = 'male', age = 20, name = 'John')
# hello_with_kwargs(gender = 'male', age = 20 )

# def func_with_args_and_kwargs(*args, **kwargs):
#     print('I would like {} {}'.format(args[0], kwargs['food']))
#
# func_with_args_and_kwargs('one', 'two', drink = 'coffee', food = 'cheese')

# Homework
def is_cat_here(*args):
    return 'cat' in [x.lower() for x in args]


print(is_cat_here('dog', 'CAT'))
print(is_cat_here('dog', 'bird'))

def is_item_here(item, *args):
    return item in args


print(is_item_here(5, 1, 2, 3, 5))
print(is_item_here('cat', 'dog', 'bird'))

def your_favorite_color(my_color, **kwargs):
    if 'color' in kwargs:
        print(f"My favorite color is {my_color}, but {kwargs['color']} is also pretty good!")
    else:
        print(f"My favorite color is {my_color}, what is your favorite color?")


your_favorite_color('blue')
your_favorite_color('red', color='green')