

tuple_1 = (1,2,3)
tuple_2 = ('one', 'hello')
tuple_3 = (3,21, 'hello')

new_tuple = (tuple_1[0], 3, tuple_1[2])
print(new_tuple)

print(tuple_1)

print(tuple_2)
print(tuple_3)

person_tuple = ('Kosta', 'Shtoiko', 2006)
first_name, last_name, year_of_birth = person_tuple
print(first_name, last_name, year_of_birth)

t1 = (1,2,3,1,1,2,5,67,22)
print(t1.count(1))
print(t1.count(8))