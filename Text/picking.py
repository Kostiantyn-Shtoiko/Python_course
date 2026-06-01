import pickle

# honda = (
#     'civic',
#     'grey',
#     '2006',
#     (
#         (1,'Roma'),
#         (2,'Kostya'),
#         (3,'Vika'),
#     )
# )

# with open ('honda.pickle', 'wb') as honda_file:
#     pickle.dump(honda, honda_file)

with open ('honda.pickle', 'rb') as honda_file:
    honda_from_file = pickle.load(honda_file)

print(honda_from_file)

model, color, year, owner_list = honda_from_file
print(model)
print(color)
print(year)
print(owner_list)
for owner in owner_list:
    owner_number, owner_name = owner
    print((owner_number, owner_name))