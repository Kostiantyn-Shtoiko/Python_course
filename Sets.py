colors = {'red','orange','green','blue'}
print(colors)
print(type(colors))

empty_set = set()
print(empty_set)
print(type(empty_set))

number_list = [1,2,43,11]
text_tuple = ('aedf', 'dfw', 'sfwwdd')

set_from_list = set(number_list)
set_from_tuple = set(text_tuple)

set_from_list.add(7653)
set_from_tuple.add('hello')

print(set_from_list)
print(set_from_tuple)