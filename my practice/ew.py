# name = input("Введите имя: ")
# print("Привет", name)
# age = input("Сколько тебе лет Рома?")
# print("Тебе", age, "лет.")
# a = int(input("Введите ваше число"))
# b = int(input("Введите ваше число"))
# print("Сумма:", a + b, "Разность:", a - b, "Произведение:", a * b, "Деление:", a / b)
# p = float(input("Начальная сумма вклада: "))
# r = float(input("Процент по вкладу: "))
# t = float(input("Количество лет: "))
# si = (p * r * t) / 100
# print("Начисленные проценты: ", si)
# c = float(input("Введите температуру в грудасах Цельсия:"))
# # f = (9/5)* c + 32
# # print(c, "градусов Цельсия равны", f, "градусам Фаренгейта")
# #
# a = 2       # число int
# b = 2.5     # число float
# c = a + b
# print(c)    # 4.5

name = ("Satanic")
def say_hi():
    name =  "Yatoro"
    print("Welcome!", name)

def say_bye():
    print("Good bye", name)

say_hi()
say_bye()

def outer():
    n = 5
    def inner():
        nonlocal n
        n = 25
        print(n)
    inner()
    print(n)
