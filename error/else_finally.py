
# while True:
#     try:
#         number = int(input('Enter some number'))
#         print(int(number) / 2)
#     except:
#         print('Not a number')
#     else:
#         print('Else block')
#         break
#     finally:
#         print('Finally block')

def divide(x,y):
    try:
        print(x / y)
    except ZeroDivisionError:
        print('division by zero')
    except TypeError:
        print('x and y must be numbers')
    else:
        print('x has been divided by y')
print(divide(4,2))
print(divide(4,0))
print(divide(4,'w'))