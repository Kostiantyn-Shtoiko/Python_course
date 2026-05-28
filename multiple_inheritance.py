# class Swimmable:
#     def __init__(self, name):
#         print('Method init() of Swimmable')
#         self.name = name
#
#     def greeting(self):
#         print(f'Hello! My name is {self.name} and I can swim')
#
#     def swim(self):
#         print('I swimming')
#
#
# class Walkable:
#     def __init__(self, name):
#         print('Method init() of Walkable')
#         self.name = name
#
#     def greeting(self):
#         print(f'Hello! My name is {self.name} and I can walk')
#
#     def walk(self):
#         print('I walking')
#
# class Flyable:
#     def __init__(self, name):
#         print('Method init() of Flyable')
#         self.name = name
#
#     def greeting(self):
#         print(f'Hello! My name is {self.name} and I can fly')
#
#     def fly(self):
#         print('I flying')
#
# class GameCharacter(Swimmable, Walkable, Flyable):
#     def __init__(self, name):
#         print('Method init() of GameCharacter')
#         self.name = name
#         Swimmable.__init__(self, name)
#         Walkable.__init__(self, name)
#         Flyable.__init__(self, name)
#
#     def greeting(self):
#         print(f'Hello! My name is {self.name}')
#
# jack = GameCharacter('Jack')
# jack.greeting()
#
# jack.swim()
# jack.walk()
# jack.fly()

# print(isinstance(jack, Flyable))
# print(isinstance(jack, Swimmable))
# print(isinstance(jack, Walkable))
# print(isinstance(jack, GameCharacter))