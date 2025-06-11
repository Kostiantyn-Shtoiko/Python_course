# Immutable
first_name = "Jake"
print(first_name[2])
#Error
    #first_name[2] = "n"
    #print(first_name)
first_two_letters = first_name[:2]
print(first_two_letters)
last_letters = first_name[-1:]
print(last_letters)
#Concatanable
new_first_name = first_two_letters + 'n' + last_letters
print(new_first_name)
# ****
print(new_first_name*2)

#---------
print(new_first_name.upper())
print(new_first_name.lower())