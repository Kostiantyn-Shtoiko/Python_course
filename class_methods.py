class Gamer:

    active_gamers = 0

    @classmethod
    def get_active_gamers(cls):
        return Gamer.active_gamers

    @classmethod
    def gamer_from_string(cls, data_string):
        nickname, age, lvl, points = data_string.split(',')
        return cls(nickname, age, lvl, points)



    def __init__(self, name, age, lvl,points):
        self.name = name
        self.age = age
        self.lvl = lvl
        self.points = points
        Gamer.active_gamers += 1

    def logout(self):
        Gamer.active_gamers -= 1

    def get_nickname(self):
        return self.name
    def get_age(self):
        return self.age
    def get_lvl(self):
        return self.lvl
    def get_points(self):
        return self.points

    def is_adult(self):
        return self.age >= 18

    def get_adult_level_permission(self):
        if self.is_adult():
            print('You can go')
        else:
            print('You not cant go')


# gamer_1 = Gamer("Gamer", 23, 5, 12)
# gamer_2 = Gamer("Gamer", 13, 6, 432)
#
# print(Gamer.active_gamers)
#
# print(gamer_1.get_age())
# gamer_1.get_adult_level_permission()
#
# print(Gamer.active_gamers)
#
# print(gamer_2.get_age())
# gamer_2.get_adult_level_permission()
#
# print(Gamer.active_gamers)
# gamer_1.logout()
# print(Gamer.active_gamers)
#
# print(Gamer.active_gamers)

# james = Gamer.gamer_from_string('James, 34, 2, 45')
# roma = Gamer.gamer_from_string('roma, 12, 6, 100')
#
# print(james.get_age())
# print(roma.get_lvl())
# print(Gamer.active_gamers)

my_dict = dict.fromkeys((1,2,3),('apple','banana','orange'))
print(my_dict)