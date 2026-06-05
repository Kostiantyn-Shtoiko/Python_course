print('hello world')
# try:
#     print(len(23))
#     print(my_variable)
# except NameError:
#     print('Some NameError')
# except TypeError:
#     print('Some TypeError')
# print('hello!!!')

user_dictionary = {'first_name':'John', 'last_name':'Doe', 'age': 25}
# print(user_dictionary['first_name'])
# print(user_dictionary.get('name'))

def get_dictionary_values(dictionary, key):
    '''
    If dictionary havent specified key, the function returns None
    :param dictionary:
    :param key:
    :return:
    '''
    try:
        return dictionary[key]
    except KeyError:
        return None

print(get_dictionary_values(user_dictionary, 'first_name'))
print(get_dictionary_values(user_dictionary, 'name'))