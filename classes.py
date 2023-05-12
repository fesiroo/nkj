# dog = 'dog'
# print(id (dog))
# print(type(dog))

# class Dog:
#     def say():
#         print('гав гав')
# Dog.say()

#     def __init__(self):
#         self.tail="один хвост "
#         self.eyes="два глаза "
#         self.paws="лапы "
#         self.nose="нос "
#         self.color=None
#         self.name=None
# ray = Dog()
# ray.color="white"
# ray.name="Ray"
# print(f"у {ray.name}, {ray.color}, {ray.eyes}, {ray.tail}, {ray.paws}, {ray.nose}")
# emma = Dog()
# emma.color="orange "
# emma.name="Emma "
# print(emma.name + emma.color + emma.nose + emma.tail + emma.paws + emma.eyes)
# norman = Dog()
# norman.color= "black "
# norman.name = "Norman "
# print(norman.name + norman.color + norman.eyes + norman.tail + norman.paws + norman.nose)

# class Apple:
#     def __init__ (self):
#         self.amount= 5
#     def eat(self, number):
#         self.amount -= number
#         return self.amount()
# apple = Apple()
# print(apple.amount)
# print(apple.eat(number=3))

class Car:
    def __init__ (self):
        self.brand =None
        self.color =None
        self.type = "легковой"
toyota = Car()
toyota.brand = "toyota"
toyota.color = "зеленый"
print("эта машина имеет следующие характеристики:")
print(f"бренд: {toyota.brand}")
print(f"цвет: {toyota.color}")
print(f"тип: {toyota.type}")
