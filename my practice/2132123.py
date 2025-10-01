# from logging.config import stopListening
#
#
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


tom = Person("Tom", 22)

print(tom.name)
print(tom.age)

tom.age = 23
#
# tom = Person("Tom", 22)
# bob = Person("Bob", 43)
#
# print(bob.name)
# print(bob.age)
#
# class Person:
#     def say(self, message):
#      print(message)
#
# tom = Person()
# tom.say("Student study")
#
#
# class Person:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# Student = Person("Roma", 17)
# print(Student.age)
# print(Student.name)
from xml.sax.handler import property_dom_node


# class Person:
#    def __init__(self, drive, stop):
#        self.drive = drive
#        self.stop = stop
# car = Person("drive", "stop")
# print(car.drive)
# print(car.stop)

# class Person:
#     def __init__(self, name):
#      def __del__(self):
#             print("Удален персонаж из игры", self.name)
# pudge = Person("Pudge")

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def print_person(self):
#          print(f"Имя: {self.name}\tВозраст: {self.age}")

class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    def set_age(self, age):
        if 0 < age < 110:
            self.__age = age
        else:
            print("Недопустимый возраст")

    def get_age(self):
        return self.__age

    def print_student(self):
        print(f"Имя: {self.name}\tВозраст: {self.__age}")







