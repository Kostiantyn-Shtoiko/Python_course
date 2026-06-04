# raise ValueError('My Invalid value')
# raise ValueError('')

# def get_rainbow_color(color_number):
#     '''
#
#     :param color_number: color number must be integer type
#     and color number must be in range of integer from 1 to 7
#     :return:
#     '''
#
#     color_number_list = [1,2,3,4,5,6,7]
#     if type(color_number) is not int:
#         raise TypeError('color number must be integer type ')
#
#     if color_number not in color_number_list:
#         raise ValueError('color number must be in range of integer from 1 to 7')
#
#     if color_number == 1:
#         return 'red'
#     elif color_number == 2:
#         return 'green'
#     elif color_number == 3:
#         return 'blue'
#     elif color_number == 4:
#         return 'yellow'
#     elif color_number == 5:
#         return 'purple'
#     elif color_number == 6:
#         return 'black'
#     elif color_number == 7:
#         return 'white'
#
# color = get_rainbow_color(0)
# print(color)

def colorize_text(color_number,text):
    '''

    :param color_number: color number must be integer type
    and color number must be in range of integer from 1 to 7
    :return:
    '''

    color_number_list = [1,2,3,4,5,6,7]
    if type(color_number) is not int:
        raise TypeError('color number must be integer type ')

    if color_number not in color_number_list:
        raise ValueError('color number must be in range of integer from 1 to 7')

    if type(text) is not str:
        raise TypeError('text must be str type')


    if color_number == 1:
        print('red ' + text)
    elif color_number == 2:
        print('yellow ' + text)
    elif color_number == 3:
        print('orange ' + text)
    elif color_number == 4:
        print('violet ' + text)
    elif color_number == 5:
        print('pink ' + text)
    elif color_number == 6:
        print('black ' + text)
    elif color_number == 7:
        print('white ' + text)

colorize_text(1,True)
