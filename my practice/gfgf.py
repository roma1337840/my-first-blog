# number = int(input("Введите количество чисел списка:"))
# numbers = []
# for i in range(number):
#     number = input(f"Введите число № {i + 1}:")
#     numbers.append(number)
# print("Ваш список", numbers)
# total = sum(numbers)
# print("Сумма чисел списка:", total)

# numbers = []
# num = int(input("Введите число"))
# while num != 0:
#     numbers.append(num)
#     num=int(input("Введите число (0 - end):"))
# print("Количество чисел:", len(numbers))

# num = int(input("Введите число:"))
# number1 = num // 1000
# number2 = (num // 100) % 10
# number3 = (num // 10) % 10
# number4 = num % 10
# print("Тысячи:", number1)
# print("Сотни:", number2)
# print("Десятки:", number3)
# print("Единицы:", number4)

# n = int(input("Введите число: "))
# x = int(input("Какую цифру искать? "))
# count = 0
# while n:
#    count += (n % 10 == x)
#    n //= 10
# print("Цифра", x, "встречается", count, "раз")

# f = open("test.txt", "w")
# f.write("Hello world!")
# f.close()

with open("hello.txt", "a") as myfile:
    print("\nhello metanit.com", file=myfile)