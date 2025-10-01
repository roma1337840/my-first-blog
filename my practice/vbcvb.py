# number = int(input("Введите число:"))
# #print("Вы ввели", number)
# numbers = []
# for i in range(number):
#     #print("Введите элемент №", i+1, ":")
#     print(f"Введите элемент № {i + 1} :")
# sp = int(input())
# numbers.append(sp)

numbers = [9, 21, 12, 1, 3, 15, 18]
sr = sum(numbers) / len(numbers)
print("Среднее арифметическое:", sr)

numbers = [-9,21,-12,1,-3,15,-18]
pos = 0
neg = 0
for n in numbers:
    if n > 0:
        pos +=1
    elif n < 0:
        neg +=1
print("Положительных чисел:", pos)
print("Отрицательных чисел:", neg)

