number_list = [32,22,1.112]
print(number_list)

some_list = [12.11, 'hello', 2]
print(some_list)
print(len(some_list))
print(some_list[1])

another_list = some_list[:2]
print(another_list)

some_list[1] = 'Kostya'
print(some_list)

new_list = some_list + another_list
print(new_list)

#Adding items
new_list.append(2764)
print(new_list)

new_list.insert(2,'Demo')
print(new_list)

#Removing items
new_list.pop(-1)
new_list.pop(0)
print(new_list)

new_list.pop(-3)
print(new_list)

# Sort
number_list = [45,5,3,-1233]
latter_list = ['w','y','v','a']

number_list.sort()
latter_list.sort()

print(number_list)
print(latter_list)

# Reverse
number_list.reverse()
latter_list.reverse()
print(number_list)
print(latter_list)

# Homework

homework_list = [1,3,412,'hello',0,'Go',65.211]
I_need_list = homework_list[1:4]
print(I_need_list)



